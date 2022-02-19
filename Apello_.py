my_file= open('data.csv','r')

#print(my_file.read())

cicli_mesi=0
cicli_anni=0
media_per_anno=0

for line in my_file:

    valore = line.split(',')        #divide il la tabella dalla data dal numero di passegeri
    print(valore[1] + ' Milioni ')
    numero=float(valore[1])
    cicli_mesi+=1
    media_per_anno+=numero

    if(cicli_mesi==12):
        cicli_mesi=0
        cicli_anni=cicli_anni + 1
        media_per_anno/=12
        print("Media dell'anno ",cicli_anni,' = ',media_per_anno, '\n')
        media_per_anno=0



my_file.close()