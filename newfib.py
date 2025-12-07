
def fib(n):
    first = 0
    second = 1
    for i in range (n):
        print (first)
        temp = first + second
        first = second
        second = temp

        ''
need = int(input("Enter number"))
fib (need)