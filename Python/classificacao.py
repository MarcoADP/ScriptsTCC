import matplotlib as plt
from sklearn import datasets
from sklearn import svm
import numpy as np

#   gamma        C    kernel    = Acertos
#0.000000001    95   default    =   72
#0.000000001    60   default    =   71
#0.000000001    100  default    =   70
#0.0000000001   100  default    =   70
#0.01           95   linear     =   117
#0.01           95   poly       =   118 degree 3 - default
#0.01           95   poly       =   118 degree 1
#0.001           95   linear     =  117

tr1 = '1'
tr2 = '3'
tst = '2'
gamma = 0.01
C = 95
kernel = 'linear'
degree = 3
degrees = [1, 2, 3]

for degree in degrees:
    if degree == 1:
        tr1 = '2'
        tr2 = '3'
        tst = '1'
    elif degree == 2:
        tr1 = '1'
        tr2 = '3'
        tst = '2'
    elif degree == 3:
        tr1 = '1'
        tr2 = '2'
        tst = '3'

    gamma = 1
    for g in range(0, 10):
        gamma = gamma/10
        C = 5;
        while C <= 100:
            if(kernel == 'poly'):
                clf = svm.SVC(gamma=gamma, C=C, kernel=kernel, degree=degree)
            else:
                clf = svm.SVC(gamma=gamma, C=C, kernel=kernel)


            DIR_TREINO = 'D:/Google Drive/TCC/Base Final/conjuntos/cruzados/'
            DIR_TESTE = 'D:/Google Drive/TCC/Base Final/conjuntos/qtd_3/'
            DIR_RESULTADO = 'D:/Google Drive/TCC/Base Final/resultados/'

            file_treino = DIR_TREINO + tr1 + "_" + tr2 + ".txt";
            file_respostas = DIR_TREINO + "respostas_" + tr1 + "_" + tr2 + ".txt";

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

            file_teste = DIR_TESTE + tst + ".txt";
            f_teste = open(file_teste, 'r');
            t = np.asarray(f_teste.read().split())
            n = t.shape[0] // 59
            t = t.reshape(n, 59)

            file_respostas = DIR_TESTE + "resposta_" + tst + ".txt";
            r_teste = open(file_respostas, 'r');
            y = np.asarray(r_teste.read().rstrip('\n').split())

            acerto = 0
            ac_classe = [0 for x in range(10)]
            ac_total = [0 for x in range(10)]
            if(kernel == 'poly'):
                f_r = DIR_RESULTADO + tst + "/" + "geral_" + str(gamma) + "_" + str(C) + "_ " + kernel + "_" + str(degree) + ".txt";
            else:
                f_r = DIR_RESULTADO + tst + "/" + "geral_" + str(gamma) + "_" + str(C) + "_ " + kernel + ".txt";

            print(f_r)
            r_g = open(f_r, 'w')

            for i in range (0, n):
                teste = t[[i]]
                #print(teste.shape)
                pr = str(clf.predict(teste))
                ac_total[int(y[i])] += 1
                #print("teste : " + str(i+1) + " PREDICAO : "  + pr + " == " + y[i])
                r_g.write(str(i+1) + ": " + pr[2] + " = " + y[i] + "\n")
                if(pr[2] == y[i]):
                    acerto = acerto + 1
                    ac_classe[int(y[i])] += 1

            #print('\n\n')
            print(str(acerto) + ' acertos de ' + str(n) + " -- aproveitamento de " + str(100*acerto/n) + '%')
            r_g.write(str(acerto) + ' acertos de ' + str(n) + " -- aproveitamento de " + str(100*acerto/n) + '%')

            print("")

            for i in range (0, 10):
                if(ac_total[i] != 0):
                    perc = ac_classe[i]/ac_total[i]
                    r_g.write("\n")
                    #print("classe [" + str(i) + "] : " + str(ac_classe[i]) + " acertos de " + str(ac_total[i]) + " -- aproveitamento de " + str(100*perc) + '%')
                    r_g.write("classe [" + str(i) + "] : " + str(ac_classe[i]) + " acertos de " + str(ac_total[i]) + " -- aproveitamento de " + str(100*perc) + '%')

            r_g.close()
            C = C + 5