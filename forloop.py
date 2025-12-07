av = 5
can = int(input('How many candy do you want to buy: '))
g = 1
while g <= can:

    if can >= av:
        av = 5
        av1 = 1
        while av1 <= av:
            print ('candy')
            av1 += 1

        print(f" can't supply {can} candy, only {av} candy available")

    print ('candy')
    g += 1
