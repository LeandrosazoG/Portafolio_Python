

#### Numeros primos#########





def is_prime():
     
    for number in range(1,101):

        if number >= 2 :

            is_divisible = False


            for i in range(2, number):
                if number % i == 0:
                    is_divisible = True
                    break
                    
            if not is_divisible:
                print(number)



is_prime()