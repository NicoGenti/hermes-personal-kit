# Contratto di delega

Per task semplice basta il campo goal. Per task non banale passa in context:

```text
RUOLO: researcher | documents | verifier
OBIETTIVO: un risultato verificabile.
INPUT: soli file, estratti, URL e preferenze necessari.
LIMITI: lettura/scrittura consentite, destinazioni, autorizzazione già ricevuta.
OUTPUT: sintesi breve, evidenze, percorsi, incertezze.
VERIFICA: condizione osservabile che distingue completato da parziale.
```

Non sono parametri aggiuntivi di delegate_task: sono testo da inserire in goal/context secondo lo schema esposto dal runtime. Non inserire segreti nel briefing.

## Report

```text
STATO: completato | parziale | bloccato
RISULTATO: ...
EVIDENZE: URL/pagine/celle/stato verificato
MODIFICHE: nessuna oppure elenco preciso
VERIFICA: esito e metodo
LIMITI: dati mancanti/errori
```

Esempio: estrarre i totali da due PDF indipendenti può essere parallelo. Spostare gli stessi file, aggiornare una memoria condivisa o controllare la stessa finestra deve essere seriale.
