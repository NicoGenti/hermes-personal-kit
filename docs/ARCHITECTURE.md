# Architettura e scelte

## Porting

Il repository originale separa router e specialisti attraverso agenti nativi OpenCode e frontmatter di modello/permessi. Hermes richiede un adattamento: questi frontmatter non sono configurazioni Hermes.

Il principale `hermes-personal-kit` mantiene instradamento, verifica e memoria. Il SOUL include brevi istruzioni dei ruoli temporanei così una delega sia autosufficiente senza caricare tutto il kit. I SOUL specialistici sono destinati a profili indipendenti successivi, non vengono caricati implicitamente da delegate_task.

## Due percorsi

| Percorso | Uso | Limite |
|---|---|---|
| hermes-personal-kit → delegate_task | Ricerche e analisi brevi | Figli con contesto nuovo, strumenti ereditati, modello globale per delegazione |
| hermes-personal-kit → Kanban → profilo specialista | Attività persistenti, configurazioni distinte, ripresa | Richiede setup Kanban/dispatcher e descrizioni dei profili |

Nel secondo percorso impostare la decomposizione Kanban manuale affinché personal crei e assegni le carte. Non presumere che `orchestrator_profile` importi il SOUL nel decompositore automatico. Un solo dispatcher per la board. Non avviare processi concorrenti sullo stesso profilo. L'abilitazione operativa del Kanban è rinviata alla verifica della versione locale.

## Strumenti e isolamento

Il profilo principale iniziale serve ricerca e coordinamento. Le capacità desktop appartengono a pc-operator. I profili separano stato, non filesystem o identità OS. Per impedire davvero la scrittura occorrono tool di sola lettura, scope API, permessi OS o sandbox. Una shell generica può aggirare una limitazione applicata solo a un tool filesystem.

Se servono strumenti locali mirati, un futuro MCP può esporre operazioni tipizzate come inventario cartella o anteprima rinomina, con validazione percorsi lato server. Questo broker non è incluso nella v0.2. Non è necessario costruirlo per verificare ricerca e delega.

## Memoria

SOUL contiene comportamento; memoria nativa contiene preferenze e fatti stabili; Kanban contiene stato delle attività quando attivato. I documenti restano nei file. Non duplicare tutto in un RAG iniziale, non usare MEMORY come registro eventi, non condividere una home Hermes tra agenti in esecuzione.

## Misurazione

Confrontare sugli stessi 5 incarichi un singolo agente e il percorso con delega. Registrare successo verificato, secondi, chiamate modello, token input/output/cache se restituiti, numero di figli e retry. Se usage manca, indicare N/D: le chiamate non equivalgono ai token. Un report breve limita il contesto del padre, non il costo del lavoro del figlio. Il routing economico va introdotto dopo la prova di qualità.

## Consapevolezza

Il comprehension-coach del kit coding diventa un resoconto operativo: risultato, azioni, destinazioni, verifica e ripristino. Non proporre un quiz dopo ogni operazione sul PC.
