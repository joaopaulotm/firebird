# D:\Python27\ python
# -*- coding: utf-8 -*-

from datetime import datetime #biblioteca de data e hora
from random import randrange #biblioteca random
import acesso #arquivo que tem a função de conectar no banco de dados e fazer a inserção de uma lista de dados

print 'starting program...'

i = 1
j = 0

print 'Time start: ' + str(datetime.now())
lista = []
while j < 10000000:

    valor = randrange(0, 50000000)
    j += 1
    if (valor > 0) and (valor < 100):
        lista.append(str(valor) + '\n')
        i += 1
        print 'value found: ' + str(valor)

print 'Total of loops: ' + str(j)

print 'Inserting records on database...' + str(datetime.now())

if lista != []:
    retorno = acesso.InsereRegistros(lista)

if retorno == 1:
    print "Full load!"
else:
    print "Some problems found..."
