# return devuelve valores que podre hcaer uso
#crear unha funcion que retorne el numero 10, y muestre por terminal si es par
def diez():
    return 10
if diez()%==0:
    print("es par")
else:
    print("es impar")
#print solo muestre por terminal

#return cuando queremos que muestre funcion devuelva o retorne un tipo dedatos  o un tipo de datos estructurados

#crear una funcion que me muestre el prodcuto de dos numeros
def producto(a,b):
    return a*b
print(producto(4,8))

#crear una funcion que me retorne una lista de tres numeros 
def lista_numeros():
    return [3,2,6]

#print usaremos cada vez que muestra funcion retorne un mensaje

#crear una funcion que por parametros reciba una nombre y retorne un mensaje de bienvenida con el nombre.
def mensaje(nombre)
    print(f"hola", {nombre} ,bienvenido al chongo")
    mensaje("jose")

#crear una funcion que reciba por parametros una lista de nunmeros y se devuelva el numero menor, mostrar por terminal el valor retornado por funcion
lista={4,3,6,78,7}
def Min(1)
   minimo=1[0]
   for n in 1:
       if n < minimo:
            minimo=n
   return minimo
   print(Min(lista))

# crear una programa que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar un diccion con los datos, luego mostar por terminal en la valor de retorno de mi funcion.
nombre=input("ingrese su nombre:")
edad=int(input("ingrese su edad":))
def persona(nom,edad):
    return{
        "nombre":nom,
        "edad":edad
    }
return dict(
    nombre=nom,
    edad=edad
)
print(persona(nombre,edad))                        

Def suma(*args):
    nueva_lista=list(args)
    nueva_lista=
    print(args)
suma (4,7,8,5,2,4)
#empaquetado y desemppaquetado de argumentos nominales 
def alumnos(**kwargs):
    kwargs["nombre"]="abel"
    print(kwargs)
alumnos(nombre="miguel",apellido="largo",edad=30)

## EJEMPLOS DE LAMBDA
saludo=lambda:"hola, {n} , {a}"
print(saludo("ruth","castillo"))

#crear un programa anonimo que reciba ccomo parametro una lista de 5 numeros y retorne dos listas una con los numeros pares y otra con numeros impares

lista=[4,7,5,3,47,2,10,8,10]
pares=lambda 1:[n for n in lista if n%2==0]
impares=lambda 1:[n for n in lista if n%2!==0]
print(pares(lista))
print(impares(lista))
tarea
    
int(input())
    def mensaje(m):
        print(m)
    def pedir:nombre():
        nombre=input("ingresa su nombre")
        return nombre
    mensaje(pedir_nombre())

#MAP
Lista=[4,7,8,5,2]
nueva_lista=maplist(lambda x:x+1,lista) #por defecto retorna una lista
print(nueva_lista)

#tengo una lista de alumnos que todos ellos aprobaron y pasan al tercer semestre,
#problema en mi lista todos estan con el segundo semestre por lo que tendremosque crear una solucion que cambie el campo
#de semestre de 2 a 3.

lista_alumnos=[
    "nombre":"abel"
    "edad":36,
    "semestre":2

    "nombre":"antohny"
    "edad":40,
    "semestre":2

    "nombre":"ediht"
    "edad":50,
    "semestre":2
]
def objetos(e)
    if "semestre" in e:
       e["semestre"]=e["semestre"]+1
    return[
        e
    ]      
def objeto(e):
5t-




    e["programa_estudio"]="APSTI"
    return[
        e
    ]            
alumnos_actualizados=list(map(,lista_alumnos))
print(alumnos_actualizados)

# FILTER
#devolver los numeros pares de una lista

lista=[4,8,2,5,7,10,6,5,3,20]
nueva_lista=list(filter(lambda x:x%2==0,lista))
print(nueva_lista)
