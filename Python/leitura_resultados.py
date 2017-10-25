import os, os.path
import numpy as np

DIR = 'D:/Google Drive/TCC/Base Final/resultados/'
DIR_OUT = DIR + 'analise/'
kernel = 'linear'

fn1 = DIR + '1/' + "#geral_" + kernel + ".txt";
fn2 = DIR + '2/' + "#geral_" + kernel + ".txt";
fn3 = DIR + '3/' + "#geral_" + kernel + ".txt";

text1 = open(fn1, 'r');
text2 = open(fn2, 'r');
text3 = open(fn3, 'r');
with open(fn1) as f:
    v1 = f.readlines()
    v1 = [x.strip() for x in v1]
with open(fn2) as f:
    v2 = f.readlines()
    v2 = [x.strip() for x in v2]
with open(fn3) as f:
    v3 = f.readlines()
    v3 = [x.strip() for x in v3]

i = 0
valores = ''
menor = 1000
perc_menor = 0
maior = 0
perc_maior = 0;
lista_soma = []

for i in range(0, len(v1)):
    if(i % 3 == 1):
        soma = int(v1[i][:3]) + int(v2[i][:3]) + int(v3[i][:3])
        perc = (soma / (133 + 134 + 133)) * 100
        valores = valores + str(soma) + ' -- ' + str(perc) + '% ' + '\n'
        lista_soma.append(soma)
        if(soma > maior):
            maior = soma
            perc_maior = perc

        if(soma < menor):
            menor = soma
            perc_menor = perc

    elif (i % 3 == 0):
        valores = valores + v1[i] + '\n'
    else:
        valores = valores + '\n';

total = 133+134+133

maximo = np.max(lista_soma)
minimo = np.min(lista_soma)
media = np.mean(lista_soma)
mediana = np.median(lista_soma)
desvio_padrao = np.std(lista_soma)
variancia = np.var(lista_soma)

#print(lista_soma)
valores = valores + "\nMaior: " + str(maximo) + " -- " + str((maximo/total)*100) + "%"
valores = valores + "\nMenor: " + str(minimo) + " -- " + str((minimo/total)*100) + "%"
valores = valores + "\nMedia: " + str(media) + " -- " + str((media/total)*100) + "%"
valores = valores + "\nMediana: " + str(mediana) + " -- " + str((mediana/total)*100) + "%"
valores = valores + "\nDesvio Padrao: " + str(desvio_padrao)
valores = valores + "\nVariancia: " + str(variancia)

filename_out = kernel + ".txt";
file_out = open(DIR_OUT + filename_out, 'w')

file_out.write(valores);
file_out.close();
