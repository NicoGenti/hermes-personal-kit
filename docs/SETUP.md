# Setup e collaudo sul PC

## Compatibilita'

Verificare `hermes --version`, `hermes profile install --help`, `hermes profile`, `hermes config --help` e `hermes tools --help`. Non esiste ancora una versione minima verificata dal kit: non e' dichiarato un requisito inventato nel manifest. In caso di comando assente, consultare la documentazione della propria release prima di aggiornare.

La documentazione upstream consultata l'8 ottobre 2026 supporta distribuzioni Git, profili indipendenti e deleghe con strumenti ereditati. Il kit usa `platform_toolsets.cli` e `agent.disabled_toolsets`; dopo l'installazione verificarne l'effetto sulla versione concreta.

## Provider

Installare la distribuzione secondo il README. Configurare il modello nel nuovo profilo con `hermes -p hermes-personal-kit model`. Non copiare l'intero config o tutti i plugin del profilo originale: si perderebbe la selezione degli strumenti del kit. Non stampare o pubblicare `.env`, auth.json o output completi di configurazione.

Ollama puo' servire modelli locali o cloud. Il solo endpoint localhost non dimostra che l'inferenza sia locale. La ricerca web puo' richiedere un backend/credenziali aggiuntivi rispetto all'accesso al modello.

## Strumenti

Aprire `hermes -p hermes-personal-kit tools` e ispezionare la selezione effettiva. CLI prevista: web, delegation, memory, session_search, todo, clarify. File, terminale, codice, browser, desktop, cron e Kanban sono disabilitati nel principale. Il toolset file include anche scrittura: non abilitarlo chiamandolo sola lettura.

Gateway e Desktop non sono configurati o collaudati da questa release. Non aggiungere plugin/MCP con permessi estesi senza rivedere la superficie del profilo. La selezione dei tool non e' isolamento OS.

Avviare la chat fuori da repository con AGENTS.md di coding: Hermes puo' ereditare contesto dal workspace anche nei figli. Non aprire processi concorrenti con la stessa home di profilo.

## Criteri di accettazione

| Controllo | PASS |
|---|---|
| Profilo | Nome e percorso attesi, distinto dal precedente |
| Modello | Provider selezionato e una risposta riuscita |
| Delega | Chiamata reale a delegate_task con risultato finale |
| Web | Richiesta al backend riuscita e fonti pertinenti |
| Superficie | Tool mutativi previsti disabilitati non esposti |
| Config | Limiti riletti correttamente dalla configurazione |

Registrare PASS, FAIL o NOT RUN. Una risposta che descrive una delega non dimostra che sia stata eseguita. Un parser YAML riuscito non certifica che Hermes usi ogni chiave. Eseguire un incarico alla volta per il primo collaudo.

## Profili specialistici

Per creare un profilo indipendente, usare per esempio `hermes profile create pc-operator`, configurarlo tramite `hermes -p pc-operator model`, individuarne il percorso con `hermes -p pc-operator profile` e copiare il relativo SOUL dopo un backup. Ripetere solo per i ruoli necessari. Non presumere che un profilo appena creato abbia strumenti ristretti: selezionarli prima del primo task.

- researcher: ricerca e confronto; strumenti web, senza shell o API mutative.
- documents: strumenti necessari ai formati e cartelle concordate; gli accessi vanno applicati negli strumenti o nell'OS, non solo nel prompt.
- pc-operator: diagnosi, poi operazioni autorizzate; verificare host/WSL/container, sessione e driver con `hermes -p pc-operator computer-use status` e `hermes -p pc-operator computer-use doctor` se disponibili.

Questi profili possono essere usati direttamente. Per farli assegnare dal principale occorre una successiva configurazione Kanban con decomposizione manuale e un dispatcher. Non esiste nel kit un parametro `delegate_task(profile=...)`. I subagenti temporanei ricevono invece un breve ruolo nel loro context.

## Rollback

Prima di un update salvare localmente SOUL/config e annotare versione/source da `hermes profile info hermes-personal-kit`. Terminare il profilo, ripristinare i file di backup e riaprire una sessione per ricaricare il prompt. I backup non vanno committati. Tornare al profilo precedente con `hermes -p NOME-PRECEDENTE chat`. Il rollback della configurazione non annulla azioni gia' eseguite sul PC o servizi esterni.
