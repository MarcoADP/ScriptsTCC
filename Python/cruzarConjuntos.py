import os.path

n_conj = 3

DIR = 'D:/Google Drive/TCC/Base Final/conjuntos/qtd_'+ str(n_conj) + '/'
DIR_OUT = 'D:/Google Drive/TCC/Base Final/conjuntos/cruzados/'

if not os.path.exists(DIR_OUT):
    os.makedirs(DIR_OUT)

for i in range (1, n_conj):
    for j in range (i,  n_conj):
        k = j + 1;
        print(str(i) + " == " + str(k))
        filename1 = DIR + str(i) + ".txt";
        filename2 = DIR + str(k) + ".txt";
        text1 = open(filename1, 'r');
        text2 = open(filename2, 'r');
        valores1 = text1.read();
        valores2 = text2.read();
        filename_out = str(i) + "_" + str(k) + ".txt";
        file_out = open(DIR_OUT + filename_out, 'w')
        file_out.write(valores1);
        file_out.write("\n");
        file_out.write(valores2)
        file_out.close();
