fib1 = int(input('Enter how many numbers you want in fibonacci series: '))
def fib (n):
    first = 0
    second = 1
    for i in range(n):
        print (first)
        temp = first
        first = second
        second = temp + first
fib(fib1)