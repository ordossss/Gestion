#Escribe una función que reciba una lista de números y devuelva su promedio.
def calcular(lista):
    # Intenta realizar la suma, si hay un error (por un tipo inválido), se lanza TypeError.
    try:
        return sum(lista) / len(lista) if lista else 0
    except TypeError:
        raise TypeError("Todos los elementos deben ser números")


print(calcular([5,10,15]))
 
#Filtrar números pares e impares haciendo uso de listas por comprension 
def filtrador(tipo,*arg):
    filtros={
        "impar":[i for i in arg if i%2!=0],
         "par":[i for i in arg if i%2==0]
            }
    return filtros.get(tipo,[]) # de get se optiene el valor de la clave tipo y lo otro es la respuesa que se espera 
    
    
a=filtrador("impar",1,2,3,4,5,6,9)
print (a)

#con PEP8 #################################################################################################################


def calcular(lista):
    """Calcula el promedio de una lista de números."""
    return sum(lista) / len(lista) if lista else 0  # Evita división por cero


def filtrador(tipo, *args):
    """Filtra números pares o impares de los argumentos proporcionados."""
    tipo = tipo.lower()  # Convierte el tipo a minúsculas para mayor flexibilidad
    filtros = {
        "impar": [num for num in args if num % 2 != 0],
        "par": [num for num in args if num % 2 == 0]
    }
    return filtros.get(tipo, [])  # Devuelve una lista vacía si el tipo no es válido


print(calcular([5, 10, 15]))  # 10.0

resultado = filtrador("impar", 1, 2, 3, 4, 5, 6, 9)
print(resultado)  # [1, 3, 5, 9]
