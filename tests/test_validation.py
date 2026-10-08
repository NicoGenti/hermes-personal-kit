"""Regression checks for accidental capability expansion and private data."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "kit"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"))

    def tearDown(self):
        self.temp.cleanup()

    def test_distribution_passes(self):
        self.assertEqual([], validator.check(self.root))

    def test_rejects_duplicate_yaml(self):
        with (self.root / "config.yaml").open("a") as f:
            f.write("\ndelegation: {}\n")
        self.assertTrue(any("Duplicate YAML" in e for e in validator.check(self.root)))

    def test_rejects_private_environment_file(self):
        (self.root / ".env").write_text("EXAMPLE=not-a-secret\n")
        self.assertTrue(any("Private file" in e for e in validator.check(self.root)))

    def test_rejects_removed_restriction(self):
        p = self.root / "config.yaml"
        p.write_text(p.read_text().replace("    - terminal\n", ""))
        self.assertTrue(any("restriction missing" in e for e in validator.check(self.root)))

    def test_rejects_increased_delegation(self):
        p = self.root / "config.yaml"
        p.write_text(p.read_text().replace("max_spawn_depth: 1", "max_spawn_depth: 3"))
        self.assertTrue(any("budget" in e for e in validator.check(self.root)))


if __name__ == "__main__":
    unittest.main()
