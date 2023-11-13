import os

anos = int (input ('Digite o valor do anos: '))
dias = int (input ('Digite o valor do dias: '))
meses = int (input ('Digite o valor do meses: '))
total_de_dias=anos*365+meses*30+dias
print ('O valor do total de dias: ' + repr (total_de_dias))
print ()
os.system ('pause')
