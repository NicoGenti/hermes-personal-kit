# Setup e collaudo

## 1. Rilevare l'ambiente

Nel terminale in cui Hermes già funziona:

```text
hermes --version
hermes --help
hermes profile
hermes profile create --help
hermes config --help
hermes tools --help
```

Usare l'help della release installata come criterio di compatibilità. Se un comando non esiste, fermare la relativa fase. Il kit non impone aggiornamenti. Annotare Windows nativo/WSL/Linux/macOS, versione, profilo attivo e percorso, modello e uso locale/cloud quando verificabile. Non condividere `.env`, chiavi, configurazioni complete o dump dell'ambiente.

## 2. Creare personal

Controllare prima che non esista già un profilo con quel nome. Sulla CLI documentata:

```text
hermes profile create personal --clone
hermes -p personal profile
```

Il clone proviene dal profilo attivo: controllarlo prima. La documentazione attuale esclude i canali di messaggistica e cron dal clone ordinario, ma include configurazione, segreti del provider, memoria curata, skill e plugin. Verificare il comportamento nella versione installata. Non usare `--clone-all` o `--clone-channels`. Se il profilo contiene integrazioni inattese, configurare un profilo vuoto tramite il setup nativo anziché copiarle indiscriminatamente.

Dal percorso effettivamente mostrato, effettuare una copia di backup locale di `SOUL.md` e `config.yaml` prima della modifica. Copiare `profiles/personal/SOUL.md` nel SOUL del nuovo profilo. Fondere `config/personal.fragment.yaml` con la configurazione esistente usando un editor YAML o il comando nativo supportato: non concatenare il frammento al fondo del file. Conservare provider, endpoint e modello. Non salvare backup con credenziali in repository o servizi condivisi.

## 3. Selezionare gli strumenti

```text
hermes -p personal tools
```

La UI e i nomi effettivi dipendono dalla release. Prima configurazione:

| Capacità | personal v0.1 |
|---|---|
| Ricerca/estrazione web | Abilitare se il backend funziona |
| Delegazione | Abilitare |
| Memoria e ricerca sessioni | Abilitare |
| Pianificazione semplice | Facoltativa |
| Terminale, esecuzione codice, scrittura file | Disabilitare nella prima prova di ricerca |
| Browser con sessioni autenticate, Computer Use | Disabilitare fino alla fase operativa |
| Invio messaggi, cron, integrazioni mutative | Disabilitare |
| MCP/plugin ereditati | Ispezionare e disabilitare quelli fuori ambito |

La separazione sopra riduce la superficie operativa: non costituisce una sandbox. La configurazione della memoria autorizza le sue scritture interne; “ricerca senza modifiche PC” non significa assenza di qualunque stato interno.

L'analisi di documenti locali diventa disponibile quando esiste uno strumento di lettura appropriato. Per PDF scansionati e creazione documenti possono servire capacità di esecuzione in un profilo dedicato; non abilitarle tacitamente sul principale.

## 4. Nuova sessione e smoke test

```text
hermes -p personal chat
```

Avviare fuori da repository con AGENTS.md di coding; i contesti workspace possono essere caricati anche nei figli. Non eseguire una seconda istanza dello stesso profilo per i test.

Inviare:

```text
Verifica quali strumenti hai realmente. Poi delega una ricerca breve a un singolo subagente: trova nella documentazione ufficiale Hermes la differenza tra profilo e subagente e restituisci due evidenze con URL. Non modificare file o configurazioni. Indica se la delega è stata realmente eseguita e se la ricerca web ha funzionato.
```

| Verifica | PASS |
|---|---|
| Avvio | Banner personal; modello/provider previsti |
| Prompt | Risposta coerente con ruolo personale, senza workflow coding obbligatorio |
| Delega | Chiamata reale a delegate_task e risultato del figlio |
| Ricerca | Fonti recuperate davvero e URL apribili |
| Permessi | Strumenti fuori ambito non esposti nella configurazione effettiva |
| Limiti | Chiavi accettate e valori riletti dalla configurazione |

Uno schema accettato non prova ancora il comportamento dei limiti in ogni percorso. Segnare NOT RUN per prove mancanti. In caso di quota/provider/tool assente riportare il problema; non dichiarare successo usando soltanto conoscenza interna.

## 5. Profili operativi, dopo il primo collaudo

Creare researcher/documents/pc-operator solo quando servono. Installare il relativo SOUL nel percorso mostrato dalla CLI, configurare modello e strumenti specifici e collaudare singolarmente. La presenza dei file nel pacchetto non attiva questi profili. Per il loro instradamento dal principale occorre configurare il Kanban nativo o un adattatore esplicito; non esiste in questo kit una chiamata magica `delegate_task(profile=...)`.

Sul profilo pc-operator verificare prima:

```text
hermes -p pc-operator computer-use status
hermes -p pc-operator computer-use doctor
```

Se il comando è supportato, il driver mancante è un prerequisito da installare separatamente. In WSL o container accertare quale desktop viene controllato. Il primo test deve limitarsi a identificare una finestra innocua concordata, senza interazione mutativa. Abilitare browser e desktop con le modalità di approvazione native; non attivare YOLO. Per operazioni ripetibili valutare il manifest di capacità supportato dal driver.

## Ripristino

Terminare la sessione personal; ripristinare SOUL.md e config.yaml dai backup corrispondenti; aprire una nuova sessione. Tornare al profilo originale con `hermes -p <nome-originale> chat`. Questo ripristino riguarda il setup, non annulla eventuali azioni svolte successivamente sul PC. Non eliminare il profilo per ripristinare due file.
