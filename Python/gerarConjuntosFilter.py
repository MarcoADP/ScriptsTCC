import os, os.path

#1   a  50 - C1
#51  a 100 - C2
#101 a 150 - C3
#151 a 200 - C4
#201 a 250 - C5
#251 a 300 - C6
#301 a 350 - C7
#351 a 400 - C8

db = '60'
LBPNeighbors = 8
LBPRadius = 2

n_classes = 8
n_audios = 5
n_pessoas = 10
n_conj = 3
audio_classe = 50;

LBPName = 'lbp' + str(LBPNeighbors) + str(LBPRadius)

#DIR = 'C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/' + LBPName + '/'+ db + '/'
DIR = 'D:/Google Drive/TCC/Base Final/' + LBPName + '/'+ db + '/'
DIR_OUT = 'D:/Google Drive/TCC/Base Final/conjuntos/qtd_'+ str(n_conj) + '/'

if not os.path.exists(DIR_OUT):
    os.makedirs(DIR_OUT)

size_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

conjuntos = ["" for x in range(n_conj+1)]
classes = ["" for x in range(n_conj+1)]

filename_out = ["" for x in range(n_conj+1)]
file_out = ["" for x in range(n_conj+1)]

for c in range(0, n_classes):
    for p in range(0, n_pessoas):
        if(p < 3):
            cj = 1
        elif(p < 6):
            cj = 2
        elif(p < 9):
            cj = 3
        else:
            resto = c % 3
            if(resto == 0):
                cj = 3
            elif(resto == 1):
                cj = 2
            else:
                cj = 1
        #pessoa: (c * n_pessoas + (p+1))  + ": " + str(cj))
        for m in range(1, n_audios + 1):
            pos = c * audio_classe + p * n_audios + m
            filename = DIR + str(pos) + ".txt";
            text = open(filename, 'r');
            valores = text.read();

            if (conjuntos[cj] != ""):
                conjuntos[cj] = conjuntos[cj] + '\n'
                classes[cj] = classes[cj] + '\n'

            print(str(pos) + " -> " + str(c) + " -- " + str(cj));
            conjuntos[cj] = conjuntos[cj] + str(valores)
            classes[cj] = classes[cj] + str(c)

for i in range(1, n_conj+1):
    f_classe_out = "resposta_" + str(i) + ".txt";
    filename_out = str(i) + ".txt";

    file_out = open(DIR_OUT + filename_out, 'w')
    file_classe_out = open(DIR_OUT + f_classe_out, 'w')

    file_out.write(conjuntos[i]);
    file_classe_out.write(classes[i])

    file_out.close();
    file_classe_out.close();