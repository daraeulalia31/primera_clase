## crear una funcion que reciba por argumentos n numeros y retorne una lista con los nuemros pares 
def numeros_pares(*args):
    pares = [num for num in args if num % 2 == 0]
    return pares

# Ejemplo de uso
resultado = numeros_pares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(resultado) 

segundo ejemplo
def num_pares(*args)
    lista_pares=[]
    for n in args:
        if n%2==0:
            lista_pares.append(n)
        return lista_pares
    #por comprension
     #return [n for n in args if n%2==0]
print(num_pares(8,5,4,7,9,25,4,7,12))

#crear 3 funciones para los siguientes casos:
#calcular el numero menor 
#calcular en numero mayor
#calcular la suma de todo los numeros 
#se le pasara por argumento n numeros

  def calcular_estadisticas(*args):
    if not args:
        return 0, 0, 0

    numero_menor = args[0]
    numero_mayor = args[0]
    suma_total = 0

    for num in args:
        if num < numero_menor:
            numero_menor = num
        if num > numero_mayor:
            numero_mayor = num
        suma_total += num

    return numero_menor, numero_mayor, suma_total

# Ejemplo de uso
numeros = 10, 5, 8, 3, 12
numero_menor, numero_mayor, suma_total = calcular_estadisticas(*numeros)

print("Número menor:", numero_menor)  # Salida: 3
print("Número mayor:", numero_mayor)  # Salida: 12
print("Suma de todos los números:", suma_total)  # Salida: 38


