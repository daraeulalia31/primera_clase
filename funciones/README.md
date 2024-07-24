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
de la funcion (micro programa) que puede contener 1 o mas sentencias, finalmente devera "retornar" un resultado con la palabra
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
# SALUDO() 
## INVOCAR FUNCIONES
para invocar una funcion (o llamar, ejecutar) una funcion solo tendremos que escribir el 'nombre' de la funcion seguido por '()' parantesis
'''python
def saludo():
    print("hola")
# INVOCAR LA FUNCION
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
cuando lo llamamos una funcion con 'argumentos', los valores de estos argumentos se copian en 
los correspondientes 'parametros' dentro de la funcion
```python
def ejem(a,b,c):
    return a+b+c
    ejem(4,5,6)
```
### ARGUMENTOS NOMINALEA
en esta aproximacion loa argumentos no son copiados en un orden especifico sino que 
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
## DESEMPAQUETADO/EMPAQUETADO DE ARGUMENTOS (TAREA) 
desempaquetado y empaquetado de argumentos se refiere a la forma en que se manejan los argumentos de una función en algunos lenguajes de programación, como Python.
 
## EMPAQUETADO DE ARGUMRNTOS:
 
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
 
## DESEMPAQUETADO DE ARGUMENTOS:
 
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
 
## EJEMPLOS DE FUNCION INTERNAS DE PYTHON:
 
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
`lambda:"hola"
El término “función lambda” significa función anónima en Python. Para crear una función lambda, Python utiliza la palabra clave lambda. Una expresión lambda consiste en la palabra clave lambda seguida de una lista de argumentos, dos puntos y una única expresión (“expression”). En cuanto se llama la función lambda, se proporciona la expresión con los argumentos y se evalúa:

### lambda argument: expression
Las funciones son una construcción lingüística fundamental de casi todos los lenguajes de programación y representan la unidad más pequeña de código reutilizable. Normalmente, las funciones en Python se definen con la palabra clave def. Por ejemplo, este también sería el caso de la función square que multiplica un número por sí mismo:

# Define square function
def square(num):
    return num * num
# Show that it works
assert square(9) == 81
python
Además de la forma más conocida de definir funciones en Python mediante la palabra clave def, el lenguaje reconoce las “lambdas”. Estas son funciones breves y anónimas (es decir, sin nombre) que definen una expresión con parámetros. Puedes utilizar las lambdas en cualquier lugar donde se espere una función o se las pueda vincular a un nombre mediante una asignación. Aquí tienes la expresión lambda equivalente a la función square:

# Create square function
squared = lambda num: num * num
# Show that it works
assert squared(9) == 81

### FUNCIONES CLOSURE
Un closure es la combinación de una función agrupada (dentro de otra) con referencias a su estado adyacente (el entorno léxico). En otras palabras, un closure te da acceso al alcance de una función externa desde una función interna. En JavaScript, los closure se crean cada vez que se crea una función, en el momento de la creación de la función.
una funcion que dentro tiene otra funcion
def saludo(nombre)
   print(f"bienvenido{nombre}")
   function init() {
  var name = "Mozilla"; // name es una variable local creada por init
  function displayName() {
    // displayName() es la función interna que forma el closure
    console.log(name); // usar la variable declarada en la función padre
  }
  displayName();
}
init();
init() crea una variable local llamada name y una función llamada displayName(). La función displayName() es una función interna que se define dentro de init() y está disponible solo dentro del cuerpo de la función init(). Tenga en cuenta que la función displayName() no tiene variables locales propias. Sin embargo, dado que las funciones internas tienen acceso a las variables de las funciones externas, displayName() puede acceder a la variable name declarada en la función principal, init().

Ejecute el código utilizando este enlace de JSFiddle y observe que la instrucción console.log() dentro de la función displayName() muestra con éxito el valor de la variable name, que se declara en su función principal. Este es un ejemplo de ámbito léxico, que describe cómo un analizador resuelve los nombres de variables cuando las funciones están anidadas. La palabra léxico se refiere al hecho de que el ámbito léxico utiliza la ubicación donde se declara una variable dentro del código fuente para determinar dónde está disponible esa variable. Las funciones anidadas tienen acceso a variables declaradas en su ámbito externo.

### FUNCIONES CALLBACK
funciones que reciben por parametro otra funcion
`int(input("ingrese un numero:))`
Una función de callback es una función que se pasa a otra función como un argumento, que luego se invoca dentro de la función externa para completar algún tipo de rutina o acción.

# Ejemplo:

JS
Copy to Clipboard
function saludar(nombre) {
  alert("Hola " + nombre);
}
function procesarEntradaUsuario(callback) {
  var nombre = prompt("Por favor ingresa tu nombre.");
  callback(nombre);
}

procesarEntradaUsuario(saludar);

### PROGRAMACION FUNCIONAL
La programación funcional (PF) es un paradigma de programación al igual que la programación orientada a objetos (POO). La PF se basa en cálculo lambda y concretamente en composición de funciones puras para modelar las soluciones de software. En cambio, la POO está más ligada a la programación imperativa y mutable (listado de instrucciones que se van ejecutando) que tienen mucha más relación con el modelo mental de Turing que hemos comentado.

El desarrollo de software va de crear soluciones a problemas pequeños y después componerlos para solucionar un problema mayor. Es por eso que un modelo basado en funciones y en composición de las mismas como únicas herramientas para crear programas, nos brinda una forma muy elocuente de crear software.

Planteemos por ejemplo el problema de querer incrementar un numero por 1. Podemos enfocar el problema creando una función que resuelva directamente el problema:

const inc = x => x + 1;
O podemos pensar en solucionar primero el problema de sumar dos números y después crear nuestra función inc mediante una composición:

const add = x => y => x + y;
const inc = add(1);
Nuestra función add toma un valor X y devuelve una función que toma otro valor Y. Finalmente devuelve la suma de los dos números.

La función inc es solo una composición (en este caso usando aplicación parcial) de add.

Si mañana tenemos que crear más funciones ‘inc’, simplemente tendremos que seguir especlializando a la función add:

const inc2 = add(2);
const inc3 = add(3);
Además, podemos crear funciones completamente nuevas componiendo varias ya existentes:

const head = arr => arr[0];
const splitBySpace = str => str.split(' ');
const firstWord = compose(head, splitBySpace);
const toUpperCase = str => str.toUpperCase();

const toUpperCaseFirstWord = compose(toUpperCase, firstWord);

toUpperCaseFirstWord('Hello World') // HELLO
# ejemplo
    if n < minimo:
         minimo
    return minimo
# programacion funcional
min(lista)

#### AVERIGUAR SOBRE MAP(). FILTER(), REDUCE()

### MAP():
Los Map en Javascript son estructuras de datos nativas que permiten implementar una estructura de tipo mapa, es decir, una estructuras donde tiene valores guardados a través de una clave para identificarlos. Comúnmente, esto se denomina pares clave-valor.

```
## EJEMPLO:

const map = new Map();                                        // Map({}) (Mapa vacío)
const map = new Map([[1, "uno"]]);                            // Map({ 1=>"uno" })
const map = new Map([[1, "uno"], [2, "dos"], [3, "tres"]]);   // Map({ 1=>"uno", 2=>"dos", 3=>"tres" })

En este ejemplo, creamos un elemento map, que no es más que un mapa de pares clave-valor. El primer map se define como un mapa vacío, el segundo, es un mapa con un solo elemento, y el tercero con 3 elementos. Para inicializar los mapas con datos, se introduce como parámetro un array de entradas (un array de arrays), que en nuestro tercer caso tiene estas combinaciones:

Clave:  1 => Valor:  "uno"
Clave:  2 => Valor:  "dos"
Clave:  3 => Valor:  "tres"
```

### FILTER():

Tal como su nombre indica filter significa filtrar, y es una de mis funciones favoritas, ya que a partir de una lista o iterador y una función condicional, es capaz de devolver una nueva colección con los elementos filtrados que cumplan la condición.

```
## ejemplo:

ef multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

filter(multiple, numeros)

<filter at 0x257ac84abe0>
Si ejecutamos el filtro obtenemos un objeto de tipo filtro, pero podemos transformarlo en una lista fácilmente haciendo un cast (conversión):


list( filter(multiple, numeros) )

[5, 10, 50]
Por tanto cuando utilizamos la función filter() tenemos que enviar una función condicional, pero como recordaréis, no es necesario definirla, podemos utlizar una función anónima lambda:


list( filter(lambda numero: numero%5 == 0, numeros) )

[5, 10, 50]
Así, en una sola línea hemos definido y ejecutado el filtro utilizando una función condicional anónima y una lista de numeros.
```
### REDUCE():

El método de reducción en su forma más simple toma dos parámetros. El primer parámetro es una función, generalmente llamada reductora, que será llamada/invocada en cada valor del array. El segundo parámetro de reduce es el valor inicial que se utilizará en la función reductora.

Ahora, la función reductora toma dos parámetros. El primer parámetro es el acumulador, que es el “valor” que irá atrapando el resultado de la función reductora, de modo que el acumulador será a lo que se reduzca el array. El segundo parámetro de la función reductora es el elemento actual en el array.

Esto es, como habrás notado, bastante difícil de explicar en texto. Así que será mejor que veamos un ejemplo de código en el que intentamos obtener el precio total de una lista de artículos.
```
# ejemplo

const items = [
  {nombre: "Arroz", precio: 5},
  {nombre: "Libro", precio: 20},
  {nombre: "Pollo", precio: 10},
  {nombre: "Monitor", precio: 100},
];

const precioTotal = items.reduce((total, item) => {
  return total + item.precio;
}, 0);
console.log(precioTotal); // 135

// precioTotal también puede ser escrito así:
const reducer = function (total, item) {
  return total + item.precio;
};
const precioTotal = items.reduce(reducer, 0);
console.log(precioTotal); // 135
```
### ACTIVIDAD

## AVERIGUAR SOBRE MODULOS Y PAQUETES EN PYTHON.

### MODULOS
Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos.

Consideremos, por ejemplo, un archivo aritmetica.py que contenga las siguientes definiciones.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
Podemos acceder a ellas desde otro archivo de Python ubicado en la misma ruta importando el módulo.

import aritmetica

print(aritmetica.sumar(7, 5))
Una sintaxis alternativa para importar objetos desde un módulo es la siguiente.

from aritmetica import sumar

print(sumar(7, 5))
Nótese que, en este segundo caso, no se prefija el nombre del módulo al invocar al objeto importado. Podemos importar varios objetos separándolos por comas.

from aritmetica import sumar, restar, mult, div

print(sumar(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))
O bien, para importar todos los objetos dentro de un módulo:

from aritmetica import *
Podemos hacer que un módulo esté visible para cualquier archivo ubicándolo en la carpeta Lib dentro del directorio de instalación de Python (p. ej. C:\Python310\Lib).
## PAQUETES
Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.

matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py
Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.

import matematica.aritmetica

print(matematica.aritmetica.sumar(7, 5))
O bien de la siguiente.

from matematica import aritmetica

print(aritmetica.sumar(7, 5))
También, esta otra:

from matematica.aritmetica import sumar

print(sumar(7, 5))
Python incluye una inmensa cantidad de módulos y paquetes en su instalación (aún más grande es aquella desarrollada por la comunidad, de la que hablaremos más adelante), a los que se conoce como librería estándar. Ahora que sabemos cómo trabajar con ellos, sopesemos esta cuestión.

## DIFERENCIAS ENTRE MODULOS Y PAQUETES.

En Python, los términos "módulos" y "paquetes" son fundamentales para organizar y estructurar el código de un programa de manera eficiente. Aquí te explico las diferencias entre ambos con ejemplos:
 
Módulos en Python:
 
- Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python. Puede contener funciones, clases y variables.
- Los módulos permiten organizar el código de forma modular para facilitar su reutilización y mantenimiento.
- Para utilizar un módulo en Python, se puede importar utilizando la palabra clave  import .
 
Ejemplo de un módulo en Python llamado  mimodulo.py :
 
python
 Copiar
# mimodulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

def sumar(a, b):
    return a + b
 
 
Paquetes en Python:
 
- Un paquete en Python es una colección de módulos relacionados que se almacenan en un directorio.
- Los paquetes permiten organizar y estructurar el código de manera jerárquica.
- Para indicar que un directorio es un paquete en Python, debe contener un archivo especial llamado  _init_.py .
 
Ejemplo de un paquete en Python llamado  mipaquete  que contiene los módulos  modulo1.py  y  modulo2.py :
 

 Copiar
mipaquete/
    _init_.py
    modulo1.py
    modulo2.py
 
 
Contenido del archivo  modulo1.py :
 
python
 Copiar
# modulo1.py
def restar(a, b):
    return a - b
 
 
Contenido del archivo  modulo2.py :
 
python
 Copiar
# modulo2.py
def multiplicar(a, b):
    return a * b
 
 
Para importar y utilizar los módulos y paquetes en Python, se pueden realizar las siguientes operaciones:
 
python
 Copiar
# Importar un módulo
import mimodulo

mimodulo.saludar("Cici")
resultado = mimodulo.sumar(3, 5)
print(resultado)

# Importar un módulo desde un paquete
from mipaquete import modulo1

resultado_resta = modulo1.restar(10, 3)
print(resultado_resta)

# Importar un paquete y un módulo desde el paquete
from mipaquete import modulo2

resultado_multiplicacion = modulo2.multiplicar(4, 6)
print(resultado_multiplicacion)
