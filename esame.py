import re                       #Importo re usata per dividere la lista in molteplici parti con la funzione re.split

class ExamException(Exception): #Classe delle eccezioni
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):   #Apertura e lettura del file
        try:
            self.name=open(name, 'r')
        except:
            raise ExamException('Error, file ({}) not found!\n'.format(name))

    def get_data(self):         #Creazione della lista di liste
       
        self.x=[]               #Nome della lista di liste(x)
        for line in self.name:
            self.data=re.split(r'-|,',line)     #Divisione del file in molteplici parti (anno, mese, valore)
            try:
                self.data[2]=self.data[2].strip()   #Cancellazione del \n alla fine di ogni riga, per evitare problemi nella conversione da stringa a float o int
                self.data[0]=int(self.data[0])      #Trasformazione di ogni parte della lista da stringa in int
                self.data[1]=int(self.data[1])

                try:
                    self.data[2]=int(self.data[2])
                    if(self.data[2]==0):
                        print('il numero e nullo, imposto il numero di default: 1\n')
                        self.data[2]=1
                except ValueError:
                    print('Non potevo convertire la stringa: "{}" in int\n'.format(self.data[2]))
                    print('Inserisco il numero di default: 1\n')
                    self.data[2]=1
                self.x.append(self.data)            #Creazione della lista di liste
            except:
                print('Il linea: "{}" non coincidone con le infomazioni neccesarie, la linea viene saltata di default.\n'.format(line.strip()))
            
            
        i=0
        for list in self.x:
            if(self.x[i][1]%12==0):
                pass
            elif(self.x[i][1]>self.x[i+1][1]):
                raise ExamException('I mesi non sono ordinati in modo corretto\n')
            elif(self.x[i][1]==self.x[i+1][1]):
                raise ExamException('Ci sono dati duplicati: {}-{},{}\n'.format(self.x[i][0],self.x[i][1],self.x[i][2]))
            i+=1
        return self.x
        
    def close_file(self):
        self.name.close()

def detect_similar_monthly_variations(time_series, years):
    media_anno_1=[]             #Array con i dati finali da confrontare
    media_anno_2=[]
    mesi_anno_1=[]              #Array che contengono i dati dei passegeri per ogni mese dell'anno
    mesi_anno_2=[]
    mese=0                      #Contatore per i mesi(per sapere su quale mese il programma si trova)
    mese_succesivo=1            #Contatore per i mesi succesivi(usato per fare la differenza tra i mesi)
    media=0                     #E la soluzione della differenza tra i mesi dello stesso anno
    test=0                      #Controlla se la diffenrenza della stessa coppia dei mesi e uguale a +-2
    soluzione=[]                #Array al quale viene assegnato il valore True o False rispetto alla condizione del test(il test deve essere maggiore uguale a -2 e minore di 2)
    for i in range(2):          #Ciclo di i per prendere gli anni nell'array years
        print(years[i] , '\n')      #Non neccesario
        try:
            index=[a for a, list in enumerate(time_series) if years[i] in list][0]                     #Cerca l'indice esatto di ogni anno in questione per poter trovare gli mesi e i dati dei passegeri
        except TypeError:
            pass
        for list in time_series:
            if years[i] in list:    #Se vienie trovato l'anno ricercato
                if(i==0):           #Condizione 1 per il primo anno
                    mesi_anno_1.append(time_series[index][2])       #Crea un array con i dati dei passegeri per ogni mese
                    print('Mese ',mese+1,': ',mesi_anno_1[mese])    #Non neccesario
                    index+=1
                    mese+=1
                elif(i==1):         #Condizione 2 per il secondo anno
                    mesi_anno_2.append(time_series[index][2])       #Crea un array con i dati dei passegeri per ogni mese
                    print('Mese ',mese+1,': ',mesi_anno_2[mese])    #Non neccesario
                    index+=1
                    mese+=1
        mese=0

    print('\n')             #Non neccesario

    for i in range(2):          #Ciclo sui 2 anni
        for a in range(11):     #Ciclo per i 12 mesi pero in coppia, cioe 11 ripetizioni
            if(i==0):           #Se siamo al primo anno
                media=mesi_anno_1[mese_succesivo]-mesi_anno_1[mese]     #Calcola se cerano piu o meno passegeri tra i passegeri per il primo anno
                media_anno_1.append(media)                              #Aggiunge il risultato alla lista per la coppia dei mesi per il primo anno
                print('media_anno_1: ',media_anno_1[mese])      #Non neccesario
                mese+=1
                mese_succesivo+=1
            else:       #Uguale al codice di sopra solo per il secondo anno
                media=mesi_anno_2[mese_succesivo]-mesi_anno_2[mese]
                media_anno_2.append(media)
                print('media_anno_2: ',media_anno_2[mese])  #Non neccesario
                mese+=1
                mese_succesivo+=1
        mese=0
        mese_succesivo=1
        print('\n')                 #Non neccesario
    
    for i in range(11):
        if(media_anno_1[mese]>media_anno_2[mese]):          #Cerca il numero piu grande tra i due risultati per evitare risultati negativi
            test=media_anno_1[mese]-media_anno_2[mese]
        else:
            test=media_anno_2[mese]-media_anno_1[mese]

        if(test>=0 and test<=2):                            #Controlla se il risultato che coincide con il problema dell'esercizio
            soluzione.append(True)
        else:
            soluzione.append(False)
        
        print('Test: la differenza= ', test)        #Non neccesario
        print(soluzione[mese])                      #Non neccesario
        mese+=1
    
    time_series_file.close_file()
    return soluzione
        

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(time_series)
try:
    years=[1950,1950]           #Gli anni ricercati
    if(years[0]+1!=years[1]):
        print('Gli anni non sono consecutivi')
        print("L'anno {} e stato cambiato in {}".format(years[1],years[0]+1))
        years[1]=years[0]+1

    for i in range(2):
        [a for a, list in enumerate(time_series) if years[i] in list][0]
except TypeError:
    pass
except IndexError:
    raise ExamException('Error, Anno "{}" non trovato'.format(years[i]))
detect_similar_monthly_variations(time_series, years)           #Accede alla funzione detect_similar_monthly_variations
print(detect_similar_monthly_variations(time_series, years))    #Non neccesario
