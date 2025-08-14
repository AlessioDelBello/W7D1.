a = ["Rosso", "Verde", "Blu", "Giallo", "Arancione", "Viola", "Nero", "Bianco"]
# la variabile a mettendola tra parentesi quadre assume il valore di una lista che in questo caso sarà una lista di colori
b = [ len(x) for x in a ]
# la variabile b assume il valore di una lista che contiene la lunghezza di ogni colore della lista a
b = []
for colore in a:
    b.append(len(colore))
# qui abbiamo aperto un ciclo for per far scorrere la lista a e per ogni colore abbiamo aggiunto alla lista b la lunghezza del colore
b =[
    {
    'colore': colore,
    'len'   :len(colore)
    }
    for colore in a
]    

for elemento in b:
    print(f"Il colore: {elemento['colore']} ha {elemento['len']}"" caratteri")  
# qui abbiamo aperto un ciclo for per far scorrere la lista b e per ogni elemento della lista b abbiamo stampato il colore e la sua lunghezza in caratteri
# la sintassi f"" permette di formattare le stringhe in modo da inserire variabili all'interno di esse, senza la f avrebbe stampato la stringa così com'è senza sostituire le variabili