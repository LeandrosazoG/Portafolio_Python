

####List Comprehesion######
my_original_list = [0,1,2,3,4,5,6,7]

my_range = range(8)
print(list(my_range))





my_list = [i + 1 for i in range(8)]
print(my_list)


my_list = [i *2  for i in range(8)]
print(my_list)


## cada numer que se guarde aqui se multiplique por si mismo 
my_list = [i * i  for i in range(8)]
print(my_list)



def sumar_five(number):
    return number +5


my_list = [sumar_five(i) for i in range(8)]
print(my_list)