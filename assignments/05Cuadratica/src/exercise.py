import math

def main():
    a = int(input("Da el valor de a: "))
    b = int(input("Da el valor de b: "))
    c = int(input("Da el valor de c: "))
    if (a == 0) and (b == 0):
        print("No tiene solucion")
    elif (a == 0) and (b != 0):
        x = -c / b
        print(x)
    elif (a != 0) and (b != 0):
        x = b**2 - 4 * a * c
        if x < 0:
            print("Raices complejas")
        elif x > 0:
            x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
            print(x1)
            x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
            print(x2)
        elif x == 0:
            x1 = -b / 2 * a
            print(x1)

if __name__ == '__main__':
    main()
