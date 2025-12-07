num = int(input("Enter a number: "))
def fib(n):
    a = 0
    b = 1
    print (a)
    print (b)

    if n == 1:
        print (b)

    elif n <= 0:
        print ("Invalid input")

    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print (c)



fib(num)