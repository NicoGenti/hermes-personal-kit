"""Static distribution checks; no Hermes runtime or model calls."""
from pathlib import Path
import re
import sys
import yaml


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def check(root):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    def read_yaml(name):
        try:
            data = yaml.load((root / name).read_text(encoding="utf-8"), Loader=UniqueLoader)
            if not isinstance(data, dict):
                raise ValueError("Expected mapping")
            return data
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{name}: {exc}")
            return {}
    manifest = read_yaml("distribution.yaml")
    config = read_yaml("config.yaml")
    require(manifest.get("name") == "hermes-personal-kit", "Unexpected distribution name")
    version = str(manifest.get("version", ""))
    require(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), "Invalid semantic version")
    require(manifest.get("env_requires") == [], "No mandatory credentials expected")
    expected_owned = ["SOUL.md", "config.yaml", "docs/", "specialists/"]
    require(manifest.get("distribution_owned") == expected_owned, "Unexpected ownership surface")
    for path in expected_owned:
        require((root / path).exists(), f"Missing distribution path: {path}")
    platforms = config.get("platform_toolsets", {})
    require(isinstance(platforms, dict), "platform_toolsets must be mapping")
    if isinstance(platforms, dict):
        require(platforms.get("cli") == ["web", "delegation", "memory", "session_search", "todo", "clarify"], "Unexpected CLI tool selection")
    required_disabled = {"terminal", "file", "code_execution", "browser", "computer_use", "cronjob", "skills", "connections", "catalog", "start_chat", "kanban"}
    agent = config.get("agent", {})
    disabled = agent.get("disabled_toolsets", []) if isinstance(agent, dict) else []
    require(isinstance(disabled, list), "disabled_toolsets must be list")
    if isinstance(disabled, list):
        require(all(isinstance(x, str) for x in disabled), "Invalid toolset name")
        if all(isinstance(x, str) for x in disabled):
            require(required_disabled <= set(disabled), "Required tool restriction missing")
    require(config.get("delegation") == {"max_concurrent_children": 2, "max_spawn_depth": 1, "orchestrator_enabled": False, "max_iterations": 20}, "Unexpected delegation budget")
    require(not ({"model", "provider", "mcp_servers"} & config.keys()), "User provider or connector config must not be bundled")
    for role in ["researcher", "documents", "pc-operator"]:
        require((root / "specialists" / role / "SOUL.md").is_file(), f"Missing role: {role}")
    changelog = root / "CHANGELOG.md"
    require(changelog.is_file() and f"## {version} " in changelog.read_text(encoding="utf-8"), "Changelog version mismatch")
    private_dirs = {"memories", "sessions", "logs", "backups", "vault", "mcp-tokens", "profiles", "state-snapshots"}
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(p in {".git", ".venv", "__pycache__", ".pytest_cache"} for p in rel.parts):
            continue
        require(not path.is_symlink(), f"Symlink in source: {rel}")
        if path.is_file():
            name = path.name.lower()
            require(not (private_dirs & set(rel.parts)), f"Private data path: {rel}")
            require(not (name.startswith(".env") or name.startswith("auth.json") or re.search(r"\.db(?:-|$)", name) or name.endswith((".pem", ".key"))), f"Private file: {rel}")
    return errors


if __name__ == "__main__":
    issues = check(Path(__file__).resolve().parents[1])
    for issue in issues:
        print(f"ERROR: {issue}", file=sys.stderr)
    if not issues:
        print("PASS: static distribution checks (runtime not tested)")
    raise SystemExit(bool(issues))
