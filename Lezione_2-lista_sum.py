def sum(my_list):
    somma=0
    for item in my_list:
        somma+=item
    return somma

my_list=[1,2,3,4,5]
print("Somma= {}".format(sum(my_list)))