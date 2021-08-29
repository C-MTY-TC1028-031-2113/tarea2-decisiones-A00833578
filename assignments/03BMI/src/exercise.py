def main():
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    if (peso <= 0) or (altura <=0):
        print(str("Revisa tus datos, alguno de ellos es erróneo."))
    else:
        indice = peso / altura**2
        if (indice < 20):
            print(str("PESO BAJO"))
        elif (indice >= 20) and (indice < 25):
            print(str("NORMAL"))
        elif (indice >= 25) and (indice < 30):
            print(str("SOBREPESO"))
        elif (indice >= 30) and (indice < 40):
            print(str("OBESIDAD"))
        elif (indice >= 40):
            print(str("OBESIDAD MORBIDA"))

if __name__=='__main__':
    main()