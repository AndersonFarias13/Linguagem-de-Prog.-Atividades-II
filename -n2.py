
#-*- coding: latin1


a = float(input('Para Saber se � Triangulo, Digite o Primeiro lado A: '))
b = float(input('Digite o Segundo  lado:B '))
c = float(input('Digite o Terceiro lado:C '))

if (a + b < c) or (a + c < b) or (b + c < a):
 print('Nao � um triangulo')
elif (a == b) and (a == c) :
 print('Tri�ngulo Equilatero ! Porque Existe dois lados iguais e um menor')
elif (a==b) or (a==c) or (b==c):
 print('Triangulo de Is�sceles ! Porque Existe dois lados iguais e um menor.')
else:
 print('Triangulo Escaleno ! Porque Todos os lados s�o diferentes')
