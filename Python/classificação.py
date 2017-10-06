import matplotlib as plt
from sklearn import datasets
from sklearn import svm
import numpy as np

#   gamma        C  = Acertos
#0.000000001    95  = 72
#0.000000001    60  = 71
#0.000000001    100 = 70
#0.0000000001   100 = 70
#0.01, C=95, kernel='linear'
clf = svm.SVC(gamma=0.01, C=95, kernel='linear')
#clf = svm.SVC()
DIR_TREINO = 'D:/Google Drive/TCC/Base Final/conjuntos/cruzados/'
DIR_TESTE = 'D:/Google Drive/TCC/Base Final/conjuntos/qtd_3/'

file_treino = DIR_TREINO + "1_2.txt";
file_respostas = DIR_TREINO + "respostas_1_2.txt";

f_treino = open(file_treino, 'r');
r_treino = open(file_respostas, 'r');


y = np.asarray(r_treino.read().rstrip('\n').split())
#print(y.shape[0])
x = np.asarray(f_treino.read().split())
x = x.reshape(y.shape[0], 59)
#print(x[59*47])
#print(x.shape)
#
clf.fit(x, y)

file_teste = DIR_TESTE + "3.txt";
f_teste = open(file_teste, 'r');
t = np.asarray(f_teste.read().split())
n = t.shape[0] // 59
t = t.reshape(n, 59)

#teste = t[[18]]

#

#teste = np.transpose(t[0].reshape(1,-1))
#teste = t[0].reshape(1,-1)
#print(teste)
#

#print(clf.n_support_)

file_respostas = DIR_TESTE + "resposta_3.txt";
r_teste = open(file_respostas, 'r');
y = np.asarray(r_teste.read().rstrip('\n').split())

acerto = 0
for i in range (0, n):
    teste = t[[i]]
    #print(teste.shape)
    pr = str(clf.predict(teste))
    print("teste : " + str(i+1) + " PREDICAO : "  + pr + " == " + y[i])
    if(pr[2] == y[i]):
        acerto = acerto + 1
    #print(clf.probA_)
    #print(clf.predict(teste))

print('\n\n')
print(str(acerto) + ' acertos de ' + str(n))
print("aproveitamento de " + str(100*acerto/n) + '%')