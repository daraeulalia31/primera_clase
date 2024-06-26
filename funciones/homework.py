## crear una funcion que reciba por argumento n numeros y retorne la lista con los numeros pares

def numeros_pares(*args):
    pares = [num for num in args if num % 2 == 0]
    return pares

# ejemplo de uso
resultado= numeros_pares(1,2,3,4,5,6,7,8,9,10)
print(resultado)

return numeros_pares
print(numeros_pares(8,5,4,7,9,25,4,7,12))

# por comprension
    #return [n for n in args if n%2==0]
print(numeros_pares(8,5,4,7,9,25,4,7,12)) 

# crear tres funcione spara los siguientes casos 
# calcular el numero menor 
# calcular el numero mayor
# calcular la suma de todos los numeros
# se le pasara por argumento n numeros

def min(**args):
    menor=args[0]
    for n in args
        if n<menor:
            menor=n
    return menor
def max(*args):
     mayor=args[0]
    for n in args
        if n<mayor:
            mayor=n
    return mayor
def sum(*args):
     suma=args[0]
    for n in args
        if n<suma:
            suma=n
    return suma

Valores=[4,7,8,5,2,]
print(Min(valores))
print(Max(valores))
print(Sum(valores))

Tarea 
Crear una lista de alumnos con los siguientes campos

#1. nombre apellido, edad, celular, email
#2. buscar el segundo registro y actualiza su edad a 50 años.

# Crear la lista de alumnos con los campos nombre, apellido, edad, celular, email
alumnos = [
    ("Juan", "Perez", 25, "123456789", "juan.perez@example.com"),
    ("Maria", "Gomez", 30, "987654321", "maria.gomez@example.com"),
    ("Pedro", "Rodriguez", 35, "456789123", "pedro.rodriguez@example.com")
]

# Función para agregar el campo "estudios" a todos los registros
def agregar_estudios(alumno):
    return alumno + ("enfermería",)

alumnos_actualizados = list(map(agregar_estudios, alumnos))

# Función para buscar y actualizar la edad del segundo registro a 50 años
def actualizar_edad(alumno):
    if alumno[0] == "Maria":
        return (alumno[0], alumno[1], 50, alumno[3], alumno[4])
    return alumno

alumnos_actualizados = list(map(actualizar_edad, alumnos_actualizados))

# Imprimir la lista actualizada de alumnos
print(alumnos_actualizados)
