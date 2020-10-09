gbp = 0.77
usd = 1.30
euro = 1.10
yen = 137.18


def menu():
    print("Currency Converter \n")
    print("Select an option to convert \n")
    print("1) GBP to USD")
    print("2) USD to GBP")
    print("3) EURO to GBP")
    print("4) GBP to EURO")
    print("5) YEN to GBP")
    print("6) GBP to YEN")
    print("7) Exit")
    
    option = int(input("Type the number of the conversion you want to use: "))
    if option == 1:
        cGBP = int(input("Please enter the amount you want to convert: "))
        print('{} GBP is {} USD\n'.format(cGBP, cGBP*usd))
        menu()

    elif option == 2:
        cUSD = int(input("Please enter the amount you want to convert: "))
        conversion = cUSD * gbp
        fee = conversion * 0.125
        print('{} USD is {} GBP\n'.format(cUSD, conversion - fee))
        menu()

    elif option == 3:
        cEURO = int(input("Please enter the amount you want to convert: "))
        conversion = cEURO * gbp
        fee = conversion * 0.125
        print('{} EURO is {} GBP\n'.format(cEURO, conversion - fee))
        menu()

    elif option == 4:
        cGBP = int(input("Please enter the amount you want to convert: "))
        print('{} GBP is {} EURO\n'.format(cGBP, cGBP*euro))
        menu()

    elif option == 5:
        cYEN = int(input("Please enter the amount you want to convert: "))
        conversion = cYEN * gbp
        fee = conversion * 0.125
        print('{} YEN is {} GBP\n'.format(cYEN, conversion - fee))
        menu()

    elif option == 6:
        cGBP = int(input("Please enter the amount you want to convert: "))
        print('{} GBP is {} YEN\n'.format(cGBP, cGBP*yen))
        menu()

    elif option == 7:
        exit()
        
    else:
        print("Choose a valid number")
        menu()

menu()
