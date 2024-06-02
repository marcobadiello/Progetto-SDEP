from Appuntamento import Appuntamento
import datetime
import calendar
from rubrica import Rubrica
class Calendario:
    def __init__(self, calendario: list[Appuntamento]):
        self.calendario= []

    def aggiungi(self, appuntamento):
        self.calendario.append(appuntamento)
    def rimuovi(self, appuntamento):
        self.calendario.remove(appuntamento)
    def appuntamenti(self):
        appuntamenti_ordinati = self.calendario.copy()
        appuntamenti_ordinati.sort(key=lambda appuntamento: (appuntamento.data, appuntamento.ora))
        for i in appuntamenti_ordinati:
            print(i)   
    def cancella_appuntamenti_scaduti(self):
            oggi = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            appuntamenti_da_cancellare = [appuntamento for appuntamento in self.calendario if appuntamento.data < oggi]

            for appuntamento in appuntamenti_da_cancellare:
                self.calendario.remove(appuntamento)    


    def cerca_appuntamenti_data(self, data):
        print("-"*50)
        appuntamenti_data = []
        for appuntamento in self.calendario:
            if appuntamento.data == data:
                appuntamenti_data.append(appuntamento)
        if len(appuntamenti_data) > 0:
            print(f"Appuntamenti del {data.strftime('%d/%m/%Y')}:")
            for appuntamento in appuntamenti_data:
                print(appuntamento)
        else:
            print(f"Non ci sono appuntamenti del {data.strftime('%d/%m/%Y')} nel calendario.")
    def stampa_appuntamenti_per_mese(self, mese,anno, Rubrica):
        num_giorni_per_mese = {
            1: 31,
            2: 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
            }
        for i in range(1,num_giorni_per_mese[mese]+1):
            data_i = str(i)+"/"+str(mese)+"/"+str(anno)
            print("-"*50)
            print(f"Appuntamenti del {data_i}")
            print("")
            data_i = datetime.datetime.strptime(data_i, "%d/%m/%Y")
            for appuntamento in self.calendario:
                if appuntamento.data == data_i:
                    print(appuntamento)
            
            if len(str(i)) == 1:
                i = str(i)
                i = "0" + i
            if len(str(mese)) == 1:
                mese = str(mese)
                mese = "0" + mese

            print("Compleanni: ")
            Rubrica.ricerca_data(data_i)


    
