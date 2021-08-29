def main():
    grados = int(input("Introduce los grados: "))
    if (grados < 0) or (grados > 360):
        print("excede")
    elif (grados == 0) or (grados == 90) or (grados == 180) or (grados == 360):
        print("eje")
    elif (grados > 0) and (grados < 90):
        print("cuadrante 1")
    elif (grados > 90) and (grados < 180):
        print("cuadrante 2")
    elif (grados > 180) and (grados < 270):
        print("cuadrante 3")
    elif (grados > 270) and (grados < 360):
        print("cuadrante 4")

if __name__ == '__main__':
    main()
