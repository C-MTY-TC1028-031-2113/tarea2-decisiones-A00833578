def main():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        id = str(input("¿Tienes identificación oficial? (s/n): "))
        if id == 's':
            print("Trámite de licencia concedido")
        elif id == 'n':
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif edad <= 0:
        print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")

if __name__ == '__main__':
    main()
