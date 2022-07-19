import collections

from Model import AmostraEntenty
from collections import ChainMap

def degrau(u):
    if u > 0:
        return 1
    return 0

def treinar(dataset):
    algoritmo = collections.ChainMap()

    algoritmo['w1'] = 1
    algoritmo['w2'] = 1
    algoritmo['w3'] = 1
    n = 1
    for x in range(1000):
        for amostra in dataset:
            elementos = amostra.split()
            u = (algoritmo['w1'] * float(elementos[0])) + (algoritmo['w2'] * float(elementos[1])) + (algoritmo['w3'] * float(elementos[2]))
            y = degrau(u)
            e = 0
            if int(float(elementos[3])) != y:
                e = degrau(int(float(elementos[3]))) - y
                algoritmo['w1'] = algoritmo['w1'] + n * e * float(elementos[0])
                algoritmo['w2'] = algoritmo['w2'] + n * e * float(elementos[1])
                algoritmo['w3'] = algoritmo['w3'] + n * e * float(elementos[2])
            #print(algoritmo)
    return algoritmo


def operacao(algoritmo, dataset):
    p1 = []
    p2 = []
    for amostra in dataset:
        elementos = amostra.split()
        u = (algoritmo['w1'] * float(elementos[0])) + (algoritmo['w2'] * float(elementos[1])) + (algoritmo['w3'] * float(elementos[2]))
        y = degrau(u)
        if y == 0:
            p1.append('Elemento: ' + str(float(elementos[0])))
        else:
            p2.append('Elemento: ' + str(float(elementos[0])))

def calcular(algoritmo, cor):
    u = (algoritmo['w1'] * cor[0]) + (algoritmo['w2'] * cor[1]) + (algoritmo['w3'] * cor[2])
    y = degrau(u)
    if y == 0:
        return 'Cor nao favoravel.'
    else:
        return 'Cor potencialmente comercializavel.'


def perceptron2String(algoritmo):
    texto = "{ Algoritmo:"
    texto += "  w1 -> " + str(float(algoritmo['w1']))
    texto += "  w2 -> " + str(float(algoritmo['w2']))
    texto += " w3 -> " + str(float(algoritmo['w3']))
    texto += " }"
    return texto

