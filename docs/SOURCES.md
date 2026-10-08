# Fonti e compatibilità

Consultate l'8 ottobre 2026. Sono documenti correnti upstream, non una certificazione della versione installata sul PC.

- Kit originale: https://github.com/NicoGenti/opencode-orchestrator-kit
- Contratto orchestratore analizzato: https://github.com/NicoGenti/opencode-orchestrator-kit/blob/main/agents/orchestrator.md
- PC Doctor analizzato: https://github.com/NicoGenti/opencode-orchestrator-kit/blob/main/extras/pc-doctor.md
- Delega: https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/
- Profili: https://hermes-agent.nousresearch.com/docs/user-guide/profiles/
- Configurazione: https://hermes-agent.nousresearch.com/docs/user-guide/configuration/
- CLI: https://hermes-agent.nousresearch.com/docs/reference/cli-commands/
- Memoria: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban/
- Computer Use: https://hermes-agent.nousresearch.com/docs/user-guide/features/computer-use
- MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/
- Ollama: https://docs.ollama.com/integrations/hermes

Scelte progettuali del kit: massimo 2 figli per batch, profondità 1, budget 20 iterazioni figlio, orchestratore capace di rispondere direttamente alle richieste semplici. Non sono benchmark o valori ottimali misurati.

Limiti verificati nella documentazione corrente: modello delegazione globale; assenza di model/toolsets per singola chiamata nel percorso documentato; profili non equivalenti a sandbox; profili specialistici e deleghe temporanee non sono la stessa identità. Verificare nuovamente se la CLI installata mostra un contratto diverso.

- Distribuzioni native: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- Toolset: https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference/

La v0.2.0 ha controlli statici, non una matrice di compatibilita runtime. Provider e modello vanno configurati nel profilo installato.
