def tarjetas(pliegos,plumones):
    
    tarjetasPliego = pliegos*12
    tarjetasPlumone = plumones*35

    if tarjetasPliego<=tarjetasPlumone:
        return tarjetasPliego
    else:
        return tarjetasPlumone

def main():
    #escribe tu código abajo de esta línea
    pli = int(input("Dame la cantidad de pliegos de papel albanene: "))
    plu = int(input("Dame la cantidad de plumones: "))

    s = tarjetas(pli,plu)

    print("El número máximo de tarjetas que se pueden hacer es:",s)

if __name__=='__main__':
    main()
