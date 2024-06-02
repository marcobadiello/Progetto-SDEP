from contatti import Contatto
from datetime import * 
class Rubrica():
    def __init__(self, rubrica: list[Contatto]):
        self.rubrica = []
    def aggiungi(self,contatto):
        self.rubrica.append(contatto)
        return(self.rubrica)
    def rimuovi(self,contatto):
        self.rubrica.remove(contatto)
    def ricerca_nome(self,name):
        l = []
        for persona in self.rubrica:
            if persona.nome == name:
                l.append(persona)
        for i in l:
            print(i)
        if len(l) == 0:
            print("Nessun nome trovato")
    def ricerca_cognome(self,sur):
        l = []
        for persona in self.rubrica:
            if persona.cognome == sur:
                l.append(persona)
        for i in l:
            print(i)
        if len(l) == 0:
            print("Nessun cognome trovato")
    def ricerca_numero(self,num):
        l = []
        for persona in self.rubrica:
            if persona.numero == num:
                l.append(persona)
        for i in l:
            print(i)
        if len(l) == 0:
            print("Nessun numero trovato")
    def ricerca_data(self,data):
        l = []
        for persona in self.rubrica:
            if persona.compleanno == data:
                l.append(persona)
        for i in l:
            print(i)    
        if len(l) == 0:
            print("Nessun compleanno trovato")
    def ricerca_multi_fattore(self, nome, cognome, numero, data):
        risultati = self.rubrica.copy()
        if nome is not None:
            risultati = [persona for persona in risultati if persona.nome == nome]
        if cognome is not None:
            risultati = [persona for persona in risultati if persona.cognome == cognome]
        if numero is not None:
            risultati = [persona for persona in risultati if persona.numero == numero]
        if data is not None:
            risultati = [persona for persona in risultati if persona.compleanno == data]
        for i in risultati:
            print(i)
        if len(risultati) == 0:
            print("Nessun risultato trovato")
        return(risultati)
    def modifica_contatto(self):
        nome = str(input("Che nome vuoi cercare: "))
        cognome = str(input("Che cognome vuoi cercare: "))
        numero = str(input("Che numero vuoi cercare: "))
        print("Compleanno: ")
        d = str(input("Giorno: "))
        m = str(input("Mese: "))
        y = str(input("Anno: "))                
        if len(d) == 1:
            d = "0" + d
        if len(m) == 1:
            m = "0" + m        
        data = datetime(int(y), int(m), int(d))
        print("Contatto trovato")
        modifica = self.ricerca_multi_fattore(nome, cognome, numero, data)[0]
        print("Vuoi modificare questo contatto: ")
        print(modifica)
        x = str(input("[Y]: sì  [N]: no : "))
        if x.upper() == "Y":
            self.rimuovi(modifica)
            print("Se non vuoi modificare un valore premi semplicemente invio")
            new_nome = str(input("Che nuovo nome vuoi salvare: "))
            new_cognome = str(input("Che nuovo cognome vuoi salvare: "))
            new_numero = str(input("Che nuovo numero vuoi salvare: "))
            if new_nome == "":
                new_nome = nome
            if new_cognome == "":
                new_cognome = cognome
            if numero == "":
                numero = numero
            x = str(input("Vuoi modificare anche il compleanno? [Y]: sì  [N]: no : "))
            if x.upper() == "Y":
                print("Nuovo Compleanno: ")
                d = str(input("Nuovo Giorno: "))
                m = str(input("Nuovo Mese: "))
                y = str(input("Nuovo Anno: "))                
                if len(d) == 1:
                    d = "0" + d
                if len(m) == 1:
                    m = "0" + m        
                new_data = datetime(int(y),int(m),int(d))      
            else: 
                new_data = data
            nuova_modifica = Contatto(new_nome,new_cognome,new_numero,new_data)
            self.aggiungi(nuova_modifica)

    def elimina(self):
        nome = str(input("Che nome: "))
        cognome = str(input("Che cognome: "))
        numero = str(input("Che numero: "))
        print("Compleanno: ")
        d = str(input("Giorno: "))
        m = str(input("Mese: "))
        y = str(input("Anno: "))                
        if len(d) == 1:
            d = "0" + d
        if len(m) == 1:
            m = "0" + m        
        data = datetime(int(y), int(m), int(d))
        print("Contatto trovato")
        modifica = self.ricerca_multi_fattore(nome, cognome, numero, data)
        if len(modifica) == 1:
            print("Sei sicuro di voler eliminare questo contatto?: ")
            modifica = self.ricerca_multi_fattore(nome, cognome, numero, data)[0]
        else:
            print("Contatto non trovato")
        x = str(input("[Y]: sì  [N]: no : "))
        if x.upper() == "Y":
            self.rimuovi(modifica) 
            print("Contatto rimosso")
