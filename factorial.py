def factorial(numer):
    if numer>=1:
 
        f=numer
        while numer>=2:
            numer=numer-1
            f=f*(numer)
        print("el factorial es: ",f)
    if numer==0:
        print("el factorial es 1")
 
 
factorial(int(input("ingrese el numero para calcular su factorial: ")))