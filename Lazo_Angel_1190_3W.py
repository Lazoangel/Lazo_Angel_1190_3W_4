print ("Lazo Jimenez Angel Jesus 3W")
def main(): #Funcion principal
    A = (input("ingresar primer valor: ")) #Esta linea es para que el usuario le de un valor a (A)
    B = (input("ingresar segundo valor: ")) #Esta linea es para que el usuario le de un valor a (B)
    C = (input("ingresar tercer valor: ")) #Esta linea es aprqa que el usuario le de un valor a (C)
    if A == B or A == C or B == C: #Compara los valores, para ver si son distintos
        print ("ALERTA los valores ingresados deben ser diferentes") #Una alerta para el usuario, (si puso valores iguales)
    else: #Indica el comienzo de un bloque
        mayor = max(A,B,C) #Es para encontrar el valor maximo 
        menor = min(A,B,C) #Es para encontrar el valor minimo
     
        print(f"El valor mayor es: {mayor}") #Imprime el valor maximo ingresado
        print(f"El valor menor es: {menor}") #Imprime el valor minimo ingresado
if __name__ == "__main__":
 main() 