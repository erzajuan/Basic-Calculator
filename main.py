def main():
    print("1. Plus (+)")
    print("2. Minus (-)")
    print("3. Time (x)")
    print("4. Divide (/)")
    choose = int(input("Your Choose  : "))
    x = float(input("First Number     : "))
    y = float(input("Second Number    : "))
    if choose == 1:
        print("Result : {}".format(x+y))
    if choose == 2:
        print("Result : {}".format(x-y))
    if choose == 3:
        print("Result : {}".format(x*y))
    if choose == 4:
        print("Result : {}".format(x/y))
    else:
        print("Invalid Operator")


if __name__ == '__main__':
    main()
