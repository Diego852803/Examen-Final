def IntroducirNumeros():
    #declaramos como globales las variables numero1 y numero2 para poder usarlas en cualquier función
    global Numero1, Numero2
    Numero1 = int(input("Introduce el primer numero: "))
    Numero2 = int(input("Introduce el segundo numero: "))

def Sumar(a, b):
    print("La Suma De: ",a," + ",b," Es ",a+b)
    
def Restar(a, b):
    print("La Resta De: ",a," - ",b," Es ",a-b)

def Multiplicar(a, b):
    print("La Multiplicacion De: ",a," * ",b," Es ",a*b)

def Dividir(a, b):
    # creamos un if para validar que el valor de “b” no sea cero, 
    # en el caso que lo fuera, lanzamos el mensaje de error al no poderse dividir entre cero.
    if b == 0:
        print("No se puede dividir entre cero")
    else:
        print("La Division De: ",a," / ",b," Es ",a/b)

while True:
    print("""
Indique el tipo de operacion que desea realizar:
1 - Sumar
2 - Restar
3 - Multiplicar
4 - Dividir
5 - Salir del programa
""")
    
    Operacion = int(input("Introduce la opcion: "))
    
    if Operacion == 1:
        IntroducirNumeros()
        Sumar(Numero1, Numero2)
    elif Operacion == 2:
        IntroducirNumeros()
        Restar(Numero1, Numero2)
    elif Operacion == 3:
        IntroducirNumeros()
        Multiplicar(Numero1, Numero2)
    elif Operacion == 4:
        IntroducirNumeros()
        Dividir(Numero1, Numero2)
    elif Operacion == 5:
        #hemos añadido break para poder salir del bucle while cuando el usuario lo decida
        break
    else:
        print("Opcion Incorrecta")