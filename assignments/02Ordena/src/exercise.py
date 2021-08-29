def main():
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if (x >= y) and (x <= z):
        print(y)
        print(x)
        print(z)
    elif (x <= y) and (x >= z):
        print(z)
        print(x)
        print(y)
    elif (y >= z) and (y <= x):
        print(z)
        print(y)
        print(x)
    elif (y > x) and (y <= z):
        print(x)
        print(y)
        print(z)
    elif (z > y) and (z < x):
        print(y)
        print(z)
        print(x)
    elif (z > x) and (z < y):
        print(x)
        print(z)
        print(y)

if __name__=='__main__':
    main()
