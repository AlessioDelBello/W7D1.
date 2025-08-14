import string
# questa comando importa il modulo string che contiene funzioni e costanti per la manipolazione delle stringhe
import random
# questa comando importa il modulo random che contiene funzioni per generare numeri o lettere casuali

ALFANUMERICI = string.ascii_letters + string.digits
# questa riga crea una variabile ALFANUMERICI che contiene tutte le lettere maiuscole e minuscole e i numeri da 0 a 9
TUTTI_ASCII = ALFANUMERICI + string.punctuation
# questa riga crea una variabile TUTTI_ASCII che contiene tutti i caratteri possibili (numeri, lettere e simboli)

def genera_password(lenght:int, charset:str) -> str:
    # qui stiamo definendo una funzione chiamata genera_password che accetta due argomenti: lenght (un intero) e charset (una stringa) il comando -> str indica che la funzione restituirà una stringa
    password = []
    # qui stiamo creando una lista vuota chiamata password che conterrà i caratteri della password generata
    for i in range(0, lenght):
        # qui stiamo creando un ciclo for che itera da 0 a lenght  per generare i caratteri della password
        lettera = random.choice(charset)
        # qui stiamo scegliendo casualmente un carattere dalla stringa charset 
        password.append(lettera)
        # qui stiamo aggiungendo il carattere scelto alla lista password
    return ''.join(password)

    # qui stiamo restituendo la password come una stringa unita, se volevamo separare i caratteri con uno | (per sempio)avremmo usato '|'.join(password

   
scelta = input("Genero una pass complessa o semplice? (c/s): ")
# qui stiamo chiedendo all'utente se vuole generare una password complessa o semplice
if scelta.lower() == 'c':
    password = genera_password(20, TUTTI_ASCII)
    # se l'utente sceglie 'c', generiamo una password complessa di 20 caratteri ASCII

elif scelta.lower() == 's': 
    password = genera_password(10, ALFANUMERICI)
    # se l'utente sceglie 's', generiamo una password semplice di 10 caratteri alfanumerici

else:
    password =  genera_password(10, ALFANUMERICI)
    # se l'utente non sceglie né 'c' né 's', genera una pass semplice di 10 caratteri alfanumerici

print(password)
# qui stiamo stampando la password generata