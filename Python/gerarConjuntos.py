import os, os.path

#1   a  50 - C1
#51  a 100 - C2
#101 a 150 - C3
#151 a 200 - C4
#201 a 250 - C5
#251 a 300 - C6
#301 a 350 - C7
#351 a 400 - C8

db = '70'
LBPNeighbors = 8
LBPRadius = 2
classes = 8
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


for i in range(1, size_files):
    classe = ((i-1) // audio_classe);
    conjunto = ((i-audio_classe*classe-1) % n_conj)+1;
    print(str(i) + " -> " + str(classe+1) + " -- " + str(conjunto));
    filename = DIR + str(i) + ".txt";
    text = open(filename, 'r');
    valores = text.read();
    conjuntos[conjunto] = conjuntos[conjunto] + str(classe+1) + " " + str(valores) + '\n';


for i in range(1, n_conj+1):
    filename_out = str(i) + ".txt";
    file_out = open(DIR_OUT + filename_out, 'w')
    file_out.write(conjuntos[i]);
    file_out.close();