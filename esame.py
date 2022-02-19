class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=open(name, 'r')

    def printlist(self):
        self.x=list(self.name)
        print(self.x)

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series_file.printlist()
#time_series = time_series_file.get_data()