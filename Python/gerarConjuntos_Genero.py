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
n_classes = 2
n_conj = 3
audio_classe = 50;

LBPName = 'lbp' + str(LBPNeighbors) + str(LBPRadius)

#DIR = 'C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/' + LBPName + '/'+ db + '/'
DIR = 'D:/Google Drive/TCC/Base Final/' + LBPName + '/'+ db + '/'
DIR_OUT = 'D:/Google Drive/TCC/Base Final/conjuntos/qtd_'+ str(n_conj) + '/'

if not os.path.exists(DIR_OUT):
    os.makedirs(DIR_OUT)

size_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(os.listdir(DIR))
print (size_files)

conjuntos = ["" for x in range(n_conj+1)]
classes = ["" for x in range(n_conj+1)]
c_atual = [0 for x in range(n_classes+1)]

for i in range(1, size_files):
    classe = ((i-1) // 50);
    classe = (classe % 2)+1

    conjunto = (c_atual[classe] % 3) + 1
    c_atual[classe] = c_atual[classe] + 1

    print(str(i) + " -> " + str(classe) + " -- " + str(conjunto));
    filename = DIR + str(i) + ".txt";
    text = open(filename, 'r');
    valores = text.read();
    #conjuntos[conjunto] = conjuntos[conjunto] + str(classe) + " " + str(valores);
    conjuntos[conjunto] = conjuntos[conjunto] + str(valores);
    classes[conjunto] = classes[conjunto] + str(classe)
    if(i < size_files-2):
        conjuntos[conjunto] = conjuntos[conjunto] + '\n'
        classes[conjunto] = classes[conjunto] + '\n'


for i in range(1, n_conj+1):
    f_classe_out = "resposta_" + str(i) + ".txt";
    filename_out = str(i) + ".txt";

    file_out = open(DIR_OUT + filename_out, 'w')
    file_classe_out = open(DIR_OUT + f_classe_out, 'w')

    file_out.write(conjuntos[i]);
    file_classe_out.write(classes[i])

    file_out.close();
    file_classe_out.close();