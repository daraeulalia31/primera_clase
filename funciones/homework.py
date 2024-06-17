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
def min(**args):
    menor=args[0]
    for n in args:
def max(*args):
    mayor=args[0]
    for n in args:
          if n>mayor:  
    return mayor                        
def sum(*args):
    suma=0
    for n in args:
       suma+=n
       return suma
valores=4,7,8,5,2,1
print(min(*valores))
print(max(*valores))
print(sum(*valores))                          