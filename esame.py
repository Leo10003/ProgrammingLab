import re

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=open(name, 'r')

    def get_data(self):
        self.x=[]
        for line in self.name:
            self.data=re.split(r'-|,',line)
            self.data[2]=self.data[2].strip()
            self.data[0]=int(self.data[0])
            self.data[1]=int(self.data[1])
            self.data[2]=int(self.data[2])
            self.x.append(self.data)
        return self.x

def detect_similar_monthly_variations(time_series, years):
    media_anno_1=[]
    media_anno_2=[]
    mesi_anno_1=[]
    mesi_anno_2=[]
    mese=0
    for i in range(2):
        print(years[i] , '\n')
        index=[a for a, lst in enumerate(time_series) if years[i] in lst][0]
        for list in time_series:
            if years[i] in list:
                if(i==0):
                    mesi_anno_1.append(time_series[index][2])
                    print('Mese ',mese+1,': ',mesi_anno_1[mese])
                    index+=1
                    mese+=1
                elif(i==1):
                    mesi_anno_2.append(time_series[index][2])
                    print('Mese ',mese+1,': ',mesi_anno_2[mese])
                    index+=1
                    mese+=1
        mese=0



time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
years=[1949,1950]
detect_similar_monthly_variations(time_series, years)
print(time_series)