from skimage.feature import local_binary_pattern
from skimage import data
import scipy
import os, os.path
import cv2

db = '80'
LBPNeighbors = 8
LBPRadius = 2

LBPName = 'lbp' + str(LBPNeighbors) + str(LBPRadius)

DIR = 'D:/Google Drive/TCC/Base Final/spectrograms/'+ db + '/'
DIR_OUT = 'D:/Google Drive/TCC/Base Final/' + LBPName + '/'+ db + '/'

#DIR = 'C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/spectrograms/'+ db + '/'
#DIR_OUT = 'C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/' + LBPName + '/'+ db + '/'

if not os.path.exists(DIR_OUT):
    os.makedirs(DIR_OUT)

size_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(os.listdir(DIR))
print (size_files)

saida = ""
for i in range(1, size_files):

    #open image
    filename = str(i) + ".png";
    print(filename)
    image = data.load(DIR + filename);
    #cv2.imshow(filename, image)

    #lbp operation
    lbp_image = local_binary_pattern(image, LBPNeighbors, LBPRadius, 'nri_uniform')
    #cv2.imshow("teste", lbp_image)
    #cv2.waitKey(2000)
    #cv2.destroyAllWindows()
    histogram = scipy.stats.itemfreq(lbp_image)

    #print(histogram.shape);
    [a, b] = histogram.shape;
    print(a)
    if(a < 59):
        print('DIFERENTE : ' + filename)
    saida = "";
    for j in range(0, a):
        #print(j)
        #print(str(histogram[j, 1]))
        #saida = saida + str(histogram[j, 0]) + ':' + str(histogram[j, 1]) + ' '
        saida = saida + str(histogram[j, 1])
        if(j < (a -1)):
            saida = saida + " "

    #saida = saida + '\n';

    filename_out = str(i) + ".txt";
    file_out = open(DIR_OUT + filename_out, 'w')
    file_out.write(saida);
    file_out.close();

#cv2.waitKey(500)
#cv2.destroyAllWindows()