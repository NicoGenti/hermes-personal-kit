# Hermes Personal Orchestrator Kit — v0.1.0

Starter per Nicolas, 8 ottobre 2026. Adatta il pattern di opencode-orchestrator-kit all'assistenza personale sul PC. Il coding rimane in OpenCode.

## Stato

Il pacchetto contiene istruzioni di profilo Hermes, contratti di delega e configurazione proposta. Non è un plugin, non installa software e non è stato eseguito sul tuo PC. Compatibilità da verificare sulla versione installata: la documentazione upstream evolve e può precedere la tua release.

## Percorso più semplice

1. Estrai questa cartella in una posizione stabile sul PC, fuori dai tuoi repository di sviluppo.
2. Apri Hermes con la configurazione Ollama che già funziona.
3. Incolla il contenuto di `AVVIO-HERMES.txt`, indicando il percorso della cartella estratta.
4. Hermes verifica l'ambiente e prepara il profilo `personal`. Il prompt autorizza le modifiche circoscritte di setup e richiede backup dei file sostituiti.
5. Apri una nuova sessione con `hermes -p personal chat` dopo la configurazione. La nuova sessione carica la nuova identità.

Non serve cambiare modello per il primo collaudo. Un endpoint Ollama locale può comunque usare un modello cloud: la posizione del server non garantisce che i dati restino sul PC.

## Contenuto

| File | Funzione |
|---|---|
| `AVVIO-HERMES.txt` | Prompt operativo per controllare e applicare il kit localmente |
| `profiles/personal/SOUL.md` | Orchestratore con instradamento e deleghe circoscritte |
| `profiles/researcher/SOUL.md` | Specialista di ricerca per un futuro profilo indipendente |
| `profiles/documents/SOUL.md` | Specialista documenti per un futuro profilo indipendente |
| `profiles/pc-operator/SOUL.md` | Specialista PC per un futuro profilo indipendente |
| `config/personal.fragment.yaml` | Limiti proposti da fondere nella configurazione, senza sostituirla |
| `docs/SETUP.md` | Setup manuale, strumenti, collaudo e ripristino |
| `docs/ARCHITECTURE.md` | Scelte e limiti del porting |
| `docs/HANDOFF.md` | Contratto breve tra orchestratore e specialisti |
| `docs/SOURCES.md` | Documentazione usata e riferimenti al kit originale |

I file `profiles/*/SOUL.md` sono prompt per Hermes, non skill installate in ChatGPT. Copiarli non crea automaticamente profili o agenti registrati. I subagenti `delegate_task` non caricano automaticamente il SOUL di un profilo omonimo: il ruolo va passato nel contesto di delega.

## Prima milestone

Profilo `personal` avviabile con il provider esistente; ricerca verificata; una delega reale conclusa; nessun accesso desktop abilitato implicitamente. Ricerca web e analisi documenti richiedono strumenti effettivamente disponibili: il solo abbonamento al modello non ne garantisce la presenza.

## Incrementi successivi

- **v0.2:** profili `documents` e `pc-operator`, accesso a cartelle concordate, collaudo browser e desktop, verifica delle modifiche e rollback.
- **v0.3:** profili sul Kanban nativo, orchestrazione manuale, un dispatcher, stato persistente.
- **v0.4:** organizzazione personale, servizi calendario/email e automazioni esplicitamente configurate.

Non sono implementati qui: broker MCP personalizzato, isolamento OS, controllo di spesa monetario, orchestrazione Kanban automatica o integrazioni con email/calendario.
