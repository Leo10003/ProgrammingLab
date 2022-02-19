class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=open(name, 'r')

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()