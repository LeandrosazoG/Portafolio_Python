
##### La sucesion de fibonacci########



def fibonacci():

    prev = 0
    next = 1

    for i in range(0,50):
        print(i)
        print(prev)
        fib = prev + next
        prev = next
        next = fib





print(fibonacci())


