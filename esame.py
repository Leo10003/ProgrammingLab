class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=open(name, 'r')

    def get_data(self):
        self.x=list(self.name)
        print(self.x)
        self.name.close()

def detect_similar_monthly_variations(time_series, years):
    pass

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
years=[1949,1950]