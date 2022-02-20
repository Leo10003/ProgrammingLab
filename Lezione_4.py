class CSVFile():
    def __init__(self, name):
        self.name=open(name,'r')
    
    def get_data(self):
        self.x=[]
        for line in self.name:
            self.data= line.split(',')

            if self.data[0] !='Date':
                self.data[1]=self.data[1].strip()
                self.x.append(self.data)
                             
        self.name.close()
        return self.x


file = CSVFile(name='shampoo_sales.csv')
File=file.get_data()
print(File)