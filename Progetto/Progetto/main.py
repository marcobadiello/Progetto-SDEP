from contatti import Contatto
from rubrica import Rubrica
from datetime import *
import csv
from hanoi import Torre
import os
from Calendario import Calendario
from Appuntamento import Appuntamento

running = True
Rubrica = Rubrica([])
Calendario = Calendario([])


def crea_stringa_data(d,m,y):
    if len(d) == 1:
        d = "0" + d
    if len(m) == 1:
        m = "0" + m        
    date = datetime(int(y),int(m),int(d))
    return(date)
def crea_stringa_ora(h,m):
    stringa = str(h)+":"+str(m)
    ora = datetime.strptime(stringa, "%H:%M").time()
    return(ora)
            
def load_data_Rubrica() -> None:
    global Rubrica
    with open('contatti.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            contatto = Contatto(row[0], row[1], str(row[2]), datetime.strptime(row[3], "%d/%m/%Y"))
            Rubrica.aggiungi(contatto)
def load_data_Calendario() -> None:
    global Calendario
    with open('appuntamenti.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data = datetime.strptime(row[1], "%d/%m/%Y")
            ora = datetime.strptime(row[2], "%H:%M").time()
            appuntamento = Appuntamento(row[0], data, ora, row[3])
            Calendario.aggiungi(appuntamento)

def save_data_Rubrica():
    global Rubrica
    with open('contatti.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Cognome", "Numero", "Compleanno"])  
        for contatto in Rubrica.rubrica:
            writer.writerow(contatto.tupla())
def save_data_Calendario():
    global Rubrica
    with open('appuntamenti.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Titolo", "Data", "Ora", "Descrizione"])  
        for appuntamento in Calendario.calendario:
            writer.writerow(appuntamento.tupla())


  
def menu():
    print("*"*50)
    print("1 ---> Rubrica")
    print("2 ---> Calendario")
    print("3 ---> Gioca")
    print("4 ---> Salva")
    print("5 ---> Esci")
    print("*"*50)
def menurubrica():
    print("*"*50)
    print("1 ---> Ricerca per Nome")
    print("2 ---> Ricerca per Cognome")
    print("3 ---> Ricerca per Numero di telefono")
    print("4 ---> Ricerca per Data di nascita")
    print("5 ---> Ricerca multi fattore")
    print("6 ---> Modifica/Elimina contatto")
    print("7 ---> Aggiungi contatto")
    print("*"*50)
def menucalendario():
    print("*"*50)
    print("1 ---> Aggiungi appuntamento")
    print("2 ---> Visualizza tutti gli appuntamenti")
    print("3 ---> Cancella appuntamenti passati")
    print("4 ---> Cerca appuntamenti per una data")
    print("5 ---> Cerca appuntamenti per un mese")
    print("*"*50)    
   
def main():
    global Rubrica
    menu()
    c = int(input("Scegli un opzione: "))
    if c == 1:
        menurubrica()
        c = int(input("Scegli un opzione: "))
        if c == 1:
            nome = str(input("Che nome vuoi cercare: "))
            Rubrica.ricerca_nome(nome)
        elif c == 2:
            sur = str(input("Che cognome vuoi cercare: "))
            Rubrica.ricerca_cognome(sur)
        elif c == 3:
            num = str(input("Che numero vuoi cercare: "))
            Rubrica.ricerca_numero(num)
        elif c == 4:
            d = str(input("Giorno: "))
            m = str(input("Mese: "))
            y = str(input("Anno: "))            
            data = crea_stringa_data(d,m,y)
            Rubrica.ricerca_data(data)
        elif c == 5:
            print("Se non sei a conoscenza di un informazione permi semplicemente invio.")
            nome = str(input("Che nome vuoi cercare: "))
            cognome = str(input("Che cognome vuoi cercare: "))
            numero = str(input("Che numero vuoi cercare: "))
            x = str(input("Vuoi cercare anche il compleanno? [Y]: sì  [N]: no : "))
            if nome == "":
                nome = None
            if cognome == "":
                cognome = None
            if numero == "":
                numero = None
            if x.upper() == "Y":
                d = str(input("Giorno: "))
                m = str(input("Mese: "))
                y = str(input("Anno: "))                
                data = crea_stringa_data()
            else:
                data = None
            Rubrica.ricerca_multi_fattore(nome, cognome, numero, data)
        elif c == 6:
            x = str(input("Vuoi rimuovere il contatto? [Y]: sì  [N]: no :"))
            if x.upper() == "Y":
                Rubrica.elimina()
            else:
        
                Rubrica.modifica_contatto()
        elif c == 7:
            nome = str(input("Che nome vuoi aggiungere: "))
            cognome = str(input("Che cognome vuoi aggiungere: "))
            numero = str(input("Che numero vuoi aggiungere: "))  
            print("Compleanno")
            d = str(input("Giorno: "))
            m = str(input("Mese: "))
            y = str(input("Anno: "))                
            data = crea_stringa_data(d,m,y) 
            persona = Contatto(nome, cognome, numero, data)
            Rubrica.aggiungi(persona)
        else:
            print("Selezionare un opzione valida!")
    elif c == 2:
        menucalendario()
        c = int(input("Scegli un opzione: "))
        if c == 1:
            titolo = str(input("Inserisci titolo: "))
            d = str(input("Inserisci giorno: ")) 
            m = str(input("Inserisci mese: "))
            y = str(input("Inserisci anno: "))
            data = crea_stringa_data(d,m,y)
            h = int(input("Inserisci ora: "))
            m = int(input("Inserisci minuti: "))
            ora = crea_stringa_ora(h,m)
            descrizione = str(input("Inserisci descrizione: "))
            Calendario.aggiungi(Appuntamento(titolo,data,ora,descrizione))
        elif c == 2:
            Calendario.appuntamenti()
        elif c == 3:
            Calendario.cancella_appuntamenti_scaduti()
        elif c == 4:
            d = str(input("Inserisci giorno: ")) 
            m = str(input("Inserisci mese: ")) 
            y = str(input("Inserisci anno: ")) 
            data = crea_stringa_data(d,m,y)
            Calendario.cerca_appuntamenti_data(data)
            print("Compleanni: ")
            Rubrica.ricerca_data(data)
        elif c == 5:
            mese = int(input("Mese: "))
            anno = int(input("Anno: "))
            Calendario.stampa_appuntamenti_per_mese(mese,anno,Rubrica)
        else:
            print("Inserire un opzione valida")
            
    elif c == 3:
        Gioco = Torre()
        Gioco.play()
    elif c == 4:
        save_data_Rubrica()
        save_data_Calendario()   
    elif c == 5:
        global running
        save_data_Rubrica()
        save_data_Calendario() 
        running = False
    else:
        print("Selezionare un opzione valida!")
print("Carico i dati...")
load_data_Rubrica()
load_data_Calendario()
print("Caricamento completato")
while running == True:
    main()
