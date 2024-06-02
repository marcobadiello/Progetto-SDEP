from contatti import Contatto
from datetime import *

class Appuntamento:
    def __init__(self,titolo: str, data: datetime, ora: datetime, descrizione: str ):
        self.titolo = titolo
        self.data = data
        self.ora = ora
        self.descrizione = descrizione


    def __str__(self):
        return("\n"+"\n"+
               "Titolo: " + str(self.titolo) + "\n"+
               "Giorno: " + str(self.data.strftime("%d/%m/%Y")) + "\n"+
               "Ora: " + str(self.ora.strftime("%H:%M")) + "\n"+
               "Descrizione: " + str(self.descrizione) + "\n"+
               "\n"+"\n"
               )
    def tupla(self):
        return (str(self.titolo), str(self.data.strftime("%d/%m/%Y")), str(self.ora.strftime("%H:%M")), str(self.descrizione))
        