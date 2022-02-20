class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=open(name, 'r')

    def get_data(self):
        self.x=[]
        for line in self.name:
            self.data=line.split(',')
            self.data[1]=self.data[1].strip()
            self.x.append(self.data)
            

        return self.x

def detect_similar_monthly_variations(time_series, years):
    for i in range(2):
        print(years[i] , '\n')
        if years[i] in time_series:
            print('1\n')

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
years=[1949,1950]
detect_similar_monthly_variations(time_series, years)
print(time_series)