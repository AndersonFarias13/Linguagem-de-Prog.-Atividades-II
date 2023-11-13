
#-*- coding: latin1


a = float(input('Para Saber se é Triangulo, Digite o Primeiro lado A: '))
b = float(input('Digite o Segundo  lado:B '))
c = float(input('Digite o Terceiro lado:C '))

if (a + b < c) or (a + c < b) or (b + c < a):
 print('Nao é um triangulo')
elif (a == b) and (a == c) :
 print('Triângulo Equilatero ! Porque Existe dois lados iguais e um menor')
elif (a==b) or (a==c) or (b==c):
 print('Triangulo de Isósceles ! Porque Existe dois lados iguais e um menor.')
else:
 print('Triangulo Escaleno ! Porque Todos os lados são diferentes')
