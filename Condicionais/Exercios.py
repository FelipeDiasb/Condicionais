# EXERCÍCIOS: 

print( '1 ----------------------------Exercício -----------------------')

# Peça para o usuário digitar um número, verifique se um número 
# é positivo, negativo ou zero.

n = int(input('Digite um número: '))

if n  ==  0:
    print('O número é correspondente a zero')  
elif n < 0: 
    print('O número é negativo')
else:
    print ('Número positivo')

print(''

'')


print( '2 ----------------------------Exercício -----------------------')
# Peça para o usuário digitar a idade, verifique 
# se uma pessoa pode votar com base na idade.
print('Verificação de  idade para votação')
idade =  int(input('Digite a idade:'))
if idade >= 18:
     print('Maior de idade')
else: 
      print('menor de idade')    

print(''

'')



print( '3 ----------------------------Exercício -----------------------')

# # Declara uma variável com um número qualquer, 
# #determine se um número é par ou ímpar.
print('Números pares e impares')
n  = int(input('Digite um número:'))

if n % 2 == 0:
    print('Par')
else:
    print('impar') 

print(''

'')





print( '4 ----------------------------Exercício -----------------------')

# # Usuário vai digitar 3  números, para criar um triângulo, 
# #verifique se um triângulo é equilátero, isósceles ou escaleno

print('Tipos de Triangolos ')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 == n2 == n3:
   print('Equilatero') 
elif n1 == n2 and  n2!= n3  or  n1== n3 and n2 != n3:
   print('Isoceles') 
else:
  print('Escaleno')



print( '5 ----------------------------Exercício -----------------------')

# # Determine se um número é múltiplo de 5 e 7.
print('Números múltiplos')
n = int(input('Digite um número:'))

if n % 5 == 0 and n % 7 ==0: 
   print('É multiplo')
else: 
   print('Não é')



print( '6 ----------------------------Exercício -----------------------')

# # Verifique se um número é positivo e maior que 10

print('Verificão se o número é maior e positivo ')
n1  =  int(input())

if  n1 > 0 and n1 >10:

    print('Esse número é mair e positivo:')  

else: 

    print('Não é')




print( '7 ----------------------------Exercício -----------------------')

# # Verifique se um número é divisível por 3 ou 5.
    
print('O número é divisível por 3 e 5')   
n4 =  int(input('Entre com um número:'))

if n4 % 3 ==0 or n4 % 5 ==0: 
    print('Divisivel')
else:
    print('Não é ')
   
   