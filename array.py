def fib(n):
    first = 0
    second = 1
    for i in range (0,n):
        print(first)
        temp = second + first
        second = first
        first = temp


fib(51)