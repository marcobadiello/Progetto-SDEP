from datetime import *
class Contatto():
    def __init__(self, nome: str, cognome: str, numero: int, compleanno: datetime):
        self.nome = nome
        self.cognome = cognome
        self.numero = numero
        self.compleanno = compleanno
        
    def __repr__(self):
        return("\n"+"\n"+
               "Nome: " + str(self.nome) + "\n"+
               "Cognome: " + str(self.cognome) + "\n"+
               "Numero di telefono: " + str(self.numero) + "\n"+
               "Compleanno: " + str(self.compleanno.strftime("%d/%m/%Y")) +
               "\n"+"\n"
               )
    def tupla(self):
        return (str(self.nome), str(self.cognome), str(self.numero), str(self.compleanno.strftime("%d/%m/%Y")))
        