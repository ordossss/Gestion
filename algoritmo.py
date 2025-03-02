# Hacer un algoritmo que muestre las tablas de multiplicar del 1 al 9 con los números del 1 a 9. 
for i in range(1,10):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}')
print('\n\n\n')
#La complejidad es O(1) ya que se conocen los limeites de los for


#Hacer un algoritmo que lea un numero entero largo e imprima la suma de sus dígitos 
numero=int(input('Digite un numero: '))
s=0
while (numero>0):
    s+=numero%10
    numero//=10

print(f'La suma es: {s}')

#La complejidad es O(logn) ya que el acumulador se reduce con // con division
print('\n\n\n')

# Hacer un algoritmo que muestre los n primeros términos de la serie de Fibonacci 
n=int(input('Digite que cantidad de numeros: '))
x=0
y=0
z=1
for i in range(n):
    x=y
    y=z
    z=x+y
    print(x)
#La complejidad es O(n) ya que hay un for y no se sabe el limite
print('\n\n\n')
# Hacer un Algoritmo que lea una palabra (cadena de caracteres) y determine si es palíndromo
cadena=input('Ingrese la palabra: ')
inicio=0
fin=len(cadena)-1
es=True
con=0

while(inicio<fin):
    con+=1
    if( cadena[inicio]!=cadena[fin]):
        es=False
    inicio+=1
    fin-=1
if es:
    print('Es palidromo')
else:
    print('No es palindromo')
print(con)
 #La complejidad es O(n) ya que el ciclo se repetira n veces    


# Hacer un algoritmo que lea un arreglo de números enteros e imprima los números que sean mayores, menores e iguales al promedio de todos los números. 

num=int(input('Digite la cantidad de numeros en el arreglo:  '))
L=[]
for i in range (num):
    a=int(input(f'Digite el numero #{i+1} :'))
    L.append(a)

menor=[]
mayor=[]
igual=[]
prom=0
sum=0
for i in range (num):
    sum+=L[i]
prom=sum//num

for i in range (num):
    if L[i]==prom:
        igual.append(L[i])
    elif L[i]>prom:
        mayor.append(L[i])
    else:
        menor.append(L[i])
print(f'Promedio: {prom}\n')
print(f'Menores:{menor} Mayores {mayor}  iguales {igual}')
#La complejidad es O(n) ya que el for se repetira n veces

# Hacer un algoritmo que lea un arreglo que contenga palabras e imprima todas las palabras que contengan, al menos una vez, una letra que seleccione el usuario 
num=int(input('Digite la cantidad de palabras en el arreglo:  '))
list=[]
for i in range (num):
    a=(input(f'Digite el numero #{i+1} :'))
    list.append(a)
word=input('Ingrese la palabra que desea buscar: ')
for i in range (num):
    if word==list[i]:
        print(list[i])
#La complejidad es O(n) ya que el for se repetira n veces



# Hacer un algoritmo  que lea dos arreglos (con el mismo número de elementos) que contengan números enteros y los combine en un tercer arreglo intercalando los elementos de los 2 arreglos leídos 
# Hacer un algoritmo que lea un arreglo con N números enteros y cree dos arreglos que contengan los números primos y los números no primos del arreglo anterior.  