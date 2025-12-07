Fib = int(input("Enter number to be printed in fibonacci: "))

def fibonacci(n):
    f = 0
    s = 1
    if n <= 0:
        print ("Invalid input")
    else:
        for i in range(n):
            print (f)
            t = f # T = 0
            f = s # f = 1
            s = t + f #0 + 1 = 1

fibonacci(Fib)

