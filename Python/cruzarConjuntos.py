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
        resposta1 = DIR + "resposta_" + str(i) + ".txt"

        filename2 = DIR + str(k) + ".txt";
        resposta2 = DIR + "resposta_" + str(k) + ".txt"

        text1 = open(filename1, 'r');
        r1 = open(resposta1, 'r')

        text2 = open(filename2, 'r');
        r2 = open(resposta2, 'r')

        valores1 = text1.read();
        vr1 = r1.read();

        valores2 = text2.read();
        vr2 = r2.read();

        filename_out = str(i) + "_" + str(k) + ".txt";
        resp_out = "respostas_" + str(i) + "_" + str(k) + ".txt";

        file_out = open(DIR_OUT + filename_out, 'w')
        r_out = open(DIR_OUT + resp_out, 'w')

        file_out.write(valores1);
        r_out.write(vr1);

        file_out.write("\n");
        r_out.write("\n");

        file_out.write(valores2)
        r_out.write(vr2);

        file_out.close();
        r_out.close();
