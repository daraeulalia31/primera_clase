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