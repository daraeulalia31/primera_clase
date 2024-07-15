# este es el script principal
import mayor_edad
def f_es_mayor(edad):
    """funcion para saber si una persona es mayor de edad"""
    if edad >=18:
        print("es mayor de edad")
    else:
        print("es menor de edad")
    
def f_es_menor(lista):
    """funcion para saber el numero menor de una lista"""
    menor=lista[0]
    for n in lista:
        if n < menor:
             menor=n
    return menor 
def f_es_mayor(lista):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n 
    return mayor
def f_cuenta_vocales(text:str):
    """funcion para contar la cantidad de vocales a que aparecen en texto"""
    text_minusculas:str=text.lower()
    cantidad_vocales=0
    for n in text_minusculas:
        if n == "a"
           cantidad_vocales+=1
    return cantidad_vocales
mayor_edad.funcion_mayor_edad(20)
print(es_menor([4,8,10,2,3]))
print(cuenta_vocales("mi mama me mima yo amo a mi mama"))

"""# este es el cript principal"""
from mayor_edad import funcion_mayor_edad
import mayor_edad
import es_mayor
import es_menor
import cuenta_vocales
mayor_edad.funcion_mayor_edad(20)
print(es_mayor.f_es_mayor([7,4,2,1,0,8]))
print(es_menor.f_es_menor([7,4,5,2,3,0]))
print(cuenta_vocales.f_cuenta_vocales("gola cosyynh lrroek"))
