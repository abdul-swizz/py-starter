def cal():
    print ('Which operator do you want to use:')
    print ("""""
    1, Addition
    2, Subtraction
    3, Multiplication
    4, Division""")
    no = int(input('Enter your choice: '))
    match no:
        case 1:
            first = input('Enter first number: ')
            while first == "":
                first = input('Enter first number: ')
                first = int(first)

            second = int(input('Enter second number: '))
            print (f"Answer = {first + second}")
        case 2:
            first = int(input('Enter first number: '))
            second = int(input('Enter second number: '))
            print (f"Answer = {first - second}")
        case 3:
            first = int(input('Enter first number: '))
            second = int(input('Enter second number: '))
            print (f"Answer = {first * second}")
        case 4:
            first = int(input('Enter first number: '))
            second = int(input('Enter second number: '))
            while second == 0:
                print ('cannot divide by zero')
                second = int(input('Enter second number: '))
            else:
                print (f"Answer = {first // second}")

cal()