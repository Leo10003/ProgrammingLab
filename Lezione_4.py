class CSVFile():
    def __init__(self, name):
        self.name=open(name,'r')
    
    def get_data(self):
        self.c=list(self.name)
        print(self.c)
        self.name.close()


file = CSVFile(name='shampoo_sales.csv')
file.get_data()
