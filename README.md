# Hermes Personal Kit

Profilo distribuibile per **Hermes Agent**: un assistente personale in italiano che coordina ricerca, analisi e attivita' sul PC. I task semplici restano al principale; quelli circoscritti e indipendenti possono essere delegati. Lo sviluppo applicativo resta in OpenCode.

**Versione 0.2.0 — distribuzione iniziale, da collaudare sul proprio Hermes.** Validazione statica inclusa; nessuna certificazione end-to-end su una specifica release Hermes. Il kit non contiene credenziali o dati personali.

## Installazione

Richiede Git e una versione Hermes che esponga `profile install`. Verifica prima:

```bash
hermes --version
hermes profile install --help
```

Dal repository pubblicato:

```bash
hermes profile install github.com/NicoGenti/hermes-personal-kit --alias
hermes -p hermes-personal-kit model
hermes -p hermes-personal-kit chat
```

Il comando `model` configura il provider per **questo nuovo profilo**. Seleziona Ollama secondo le opzioni della tua release, mantenendo il modello che gia' usi. L'installazione non eredita automaticamente la configurazione creata da `ollama launch hermes`. Non sostituire l'intero config del kit con quello del profilo precedente.

Per un checkout o un archivio estratto, prima della pubblicazione:

```bash
hermes profile install /percorso/assoluto/hermes-personal-kit --alias
```

Se il profilo esiste gia', controlla `hermes profile info hermes-personal-kit` e segui il percorso di aggiornamento. Non sostituire un profilo personale diverso con lo stesso nome.

## Funziona gia' / richiede attivazione

| Capacita' | Stato nella distribuzione |
|---|---|
| Instradamento e risposta in italiano | Prompt principale |
| Ricerca web | Toolset selezionato; richiede backend disponibile |
| Subagenti temporanei | Delegation selezionato; prova reale necessaria |
| Memoria e ricerca sessioni | Strumenti nativi selezionati |
| Lettura/scrittura documenti locali | Disabilitata nel principale; template specialista |
| Browser autenticato e controllo desktop | Disabilitati nel principale; attivazione in profilo separato |
| Profili specialistici persistenti | Template inclusi, non registrati automaticamente |
| Kanban, email e cron | Non attivati |

La prima release abilita la base di ricerca/coordinamento. Non promette controllo del PC senza configurare e verificare i suoi strumenti. I prompt specialistici non sono sandbox e non cambiano i permessi OS.

## Primo collaudo

In una nuova chat del profilo:

> Delega a un solo subagente una ricerca sulle differenze tra profilo e subagente nella documentazione ufficiale Hermes. Restituisci due evidenze con URL. Indica se delega e web sono stati realmente usati. Non modificare configurazioni.

Controlla le chiamate effettive e il risultato. Se uno strumento manca, la prova e' bloccata, non riuscita. Vedi [setup e collaudo](docs/SETUP.md).

## Aggiornamento

```bash
hermes profile update hermes-personal-kit
```

Hermes preserva normalmente la configurazione locale; una nuova versione del config nel repository potrebbe quindi richiedere una fusione manuale. Non usare `--force-config` senza backup: puo' ripristinare i default e perdere le scelte locali. Memoria, sessioni e credenziali non appartengono alla distribuzione. Personalizza in modo consapevole i file distribuiti: SOUL e documenti possono essere sostituiti dagli aggiornamenti.

## Struttura

- `distribution.yaml`: manifest nativo Hermes.
- `SOUL.md`: orchestratore e briefing dei ruoli temporanei.
- `config.yaml`: strumenti e limiti del profilo principale.
- `specialists/`: SOUL per profili separati da creare esplicitamente.
- `docs/`: setup, architettura, contratto e fonti.
- `scripts/validate.py`: controllo statico di manifest, config e contenuti pubblicabili.
- `.github/workflows/validate.yml`: verifica automatica su push e pull request.

## Validazione per contributori

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

La CI non esegue modelli a pagamento, non richiede segreti e non prova il desktop. Per versionare: aggiornare `distribution.yaml` e `CHANGELOG.md`, validare, collaudare sulla release Hermes indicata e solo dopo creare il tag.

## Provenienza

Ispirato al pattern di [opencode-orchestrator-kit](https://github.com/NicoGenti/opencode-orchestrator-kit): deleghe precise, contesto piccolo, verifiche e risultati tracciabili. Adattamento specifico a Hermes; non importa agenti o permessi OpenCode. [Fonti e limiti](docs/SOURCES.md).
