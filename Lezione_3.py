my_list=open('shampoo_sales.csv', 'r')

somma=0


for line in my_list:

    elements = line.split(',')
    print(elements[1])
    value=float(elements[1])
    
    somma+=value

print(somma)

my_list.close()