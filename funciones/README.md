# FUNCIONES
matematicamente una funcion es una ioperacion que toma uno o mas valores llamados a ´argumentos´ y produce un valor denominado ´resultado´
# FUNCIONES
matematicamente una funcion es una operacion 
que toma uno om mas valores llamados´argumentos´
y produce un valor denominado resultado.
f(x)=x/1+x**2
>[!NOTE]
>todos los lenguajes de programacion tienen 
funciones incorporadas (funciones internas), y funciones creadas por el usuario (fuciones externas)
en programacion una funcion es un subprograma, es una estrutura que nos permite agrupar codigo y sus principales objetivos son 
-´no repetir´ fragmetos de codigos 
-reutilizar´ el codigo en distitos esenarios 
## ESTRUCTURA DE FUNCION
##definir una funcion en python
para definir una funcion en paython primero utilizaremos la palabra reservada "def" seguida po el "nombre" de la funcion. a 
continuacionespecificaremos los "parametros" con "()" si es una funcion con parametros, si se tuviera ,as de un parametros
iran separados por ",", finalizando la linea con ":", en la siguiente linea sin olvidar el identado, comenzara el "cuerpo"
de la funcion (micro progrma) que puede contener 1 o mas sentencias, finalmente devera "retornar" un resultado con la palabra
´return´.
[!INFO]
como retorno tambien se puede utilizar la "funcion interna". "print ()", ´para depuracion de codigo no es recomendable usarlo en produccion.
**EJEMPLO**
´´´Python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return F"{saludo}, {saludo_dos}
    #print(f"{saludo}, {saludo_dos})
print(saludo())
# saludo()
## INVOCAR FUNCIONES
para invocar una funcion (o llamar, ejecutar) una funcion solo tendremos que escribir el 'nombre' de la funcion seguido por '()' parantesis
'''python
def saludo():
    print("hola")
# invocar la funcion
saludo()
'''
## RETORMAR VALOR 
las funciones pueden retornar (o devolver) un valor.
'''python
def uno():
    return 1
uno()
'''
[!WARNING]
no confundir 'print()' con 'return', el valor retornado por 'return' nos permite usarlo fuera de su contexto, y 'print()' solo mostrara
el literal por terminal.
**ejemplo**
*en el archivo 'lecture.py'
## RETORNANDO MULTIPLES VALORES
 el secreto es hacerlo mediante un un tipo de dato estructurado.
 '''python
 def varios():
     return 2,3,4
 varios()
 # retorna (2,3,4,)
 def lista():
     return ["hola", 45]
lista()
# retorna ["hola",45]
def dicc():
     return {"nombre":"jose","edad":45}
return - tipo de datos
         tipo de dato estructurado
print - mensaje 
'''
## PARAMETROS Y ARGUMENTOS 
si una funcion no dispusiera de valores de entreda estaria limitada en su actuacion.
es por ello que los 'parametros' no permiten variar los datos que consume una funcion 
para obtener distintos resultados
**ejemplos**
#crear una funcion que recibe un valor numerico y devuelve su raiz cuadrada*
```python
def sqrtr(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)
```
cuando lo llamamos una funcion con 'argumentos', los valores de estos atgumentos se copian en 
los correspondientes 'parametros' dentro de la funcion
```python
def ejem(a,b,c):
    return a+b+c
    ejem(4,5,6)
```
### ARGUMENTOS NOMINALEA
en est aproximacion loa argumentos no son copiados en un orden especifico sino que 
**se asiganan por nombre a cada parametro**. ellos nos permite evitar el problema de 
conocer o recordar cual es el orden de los parametros de la defincion de la funcion.
Para utilizarlo, basta con realizar una asignacion de cada argumemto en la propia 
llamada de la funcion.
**ejemplos**
```python
def buil_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia},
    con {num_core} cores y con una
    frecuencia de {frecuencia}
    """)
    #haciendo uso de argumentosnominales
    build_cup(num_core=4,familia="intrel",frecuencia=2.7)

```
### ARGUMENTOS POSICIONALES
los argumentos son copiados en un orden especifico, en este caso debemos conocer o 
recordar cual es el orden de los parametros.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    la cpu es la familia {familia},
    con {num_core} cores y con una 
    frecuencia de {frecuencia}
    """)
```
# haciendo uso de argumentos posicionales
bull_cup("intel", 4,2,7)

### PARAMETROS POR DEFECTO
es posible especificar **valores por defecto** en los parametros de una funcion, en el caso de que no se 
proporcione en valor el argumento en la llamada a la funcion, el parametro correspondiente tomara el valor
defimido por defecto.
**ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):
    alumnos("ruth"."castillo")
    alumonos("anthony","crucez","desaprobado")
```
## desempaquetado/empaquetado de argumentos(tarea)
desempaquetado y empaquetado de argumentos se refiere a la forma en que se manejan los argumentos de una función en algunos lenguajes de programación, como Python.
 
## Empaquetado de Argumentos:
 
En el empaquetado de argumentos, se pueden pasar múltiples argumentos a una función como una sola variable. Esto se logra utilizando el operador  *  antes del nombre de la variable en la definición de la función. Por ejemplo:
 
python
 Copiar
def sumar(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

resultado = sumar(1, 2, 3, 4)
print(resultado)  # Salida: 10
 
 
En este ejemplo, la función  sumar  puede recibir cualquier cantidad de argumentos y los trata como una tupla llamada  numeros .
 
## Desempaquetado de Argumentos:
 
El desempaquetado de argumentos se utiliza cuando se quiere pasar una lista o tupla de valores como argumentos individuales a una función. Esto se logra utilizando el operador  *  antes del nombre de la lista o tupla al llamar a la función. Por ejemplo:
 
python
 Copiar
def saludar(nombre, apellido):
    return f"Hola {nombre} {apellido}!"

datos = ["Juan", "Perez"]
mensaje = saludar(*datos)
print(mensaje)  # Salida: Hola Juan Perez!
 
 
En este caso, la lista  datos  se desempaqueta y se pasa como dos argumentos individuales a la función  saludar .
 
El empaquetado y desempaquetado de argumentos son útiles para trabajar con un número variable de argumentos en funciones y para pasar valores contenidos en listas o tuplas como argumentos individuales

## FUNCIONES INTRERNAS DE PYTHON(tareas)
    En Python, las funciones internas son funciones predefinidas en el lenguaje que están disponibles para su uso sin necesidad de importar ningún módulo adicional. Algunas de las funciones internas más comunes en Python son  print() ,  len() ,  type() ,  range() ,  max() ,  min() , entre otras.
 
## Ejemplos de Funciones Internas de Python:
 
 ## Función  print() : Imprime un mensaje en la consola.
 
python
 Copiar
print("Hola, mundo!")
 
## Función  len() : Devuelve la longitud de un objeto (por ejemplo, una lista, tupla, cadena, etc.).
 
python
 Copiar
lista = [1, 2, 3, 4, 5]
print(len(lista))  # Salida: 5

## Función  type() : Devuelve el tipo de un objeto.
 
python
 Copiar
numero = 10
print(type(numero))  # Salida: <class 'int'>
 
## Función  range() : Genera una secuencia de números.
 
python
 Copiar
for i in range(1, 5):
    print(i)
# Salida: 1, 2, 3, 4
 
## Función  max()  y  min() : Devuelven el valor máximo y mínimo de una secuencia de números.
 
## python
 Copiar
numeros = [10, 5, 20, 15]
print(max(numeros))  # Salida: 20
print(min(numeros))  # Salida: 5
 
 
Estas son solo algunas de las muchas funciones internas útiles que Python proporciona de forma predeterminada. Puedes explorar más funciones internas en la documentación oficial de Python.                                                                                                                                        

## TIPOS DE FUNCIONES
### FUNCIONES ANONIMAS (FUNCIONES LAMBDA)
### FUNCIONES CLOSURE
### FUNCIONES CALLBACK
### PROGRAMACION FUNCIONAL
