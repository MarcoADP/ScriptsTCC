from skimage.feature import local_binary_pattern
from skimage import data
import scipy
import os, os.path
import cv2

db = '55'

DIR = 'C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/spectrograms/'+ db + '/'
DIR_OUT = 'C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/lbp/'+ db + '/'

if not os.path.exists(DIR_OUT):
    os.makedirs(DIR_OUT)

size_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(os.listdir(DIR))
print (size_files)

for i in range(1, size_files):
    #open image
    print(i)
    filename = str(i) + ".png";
    print(filename)
    image = data.load(DIR + filename);
    cv2.imshow(filename, image)

    #lbp operation
    lbp_image = local_binary_pattern(image, 8, 2, 'nri_uniform')
    histogram = scipy.stats.itemfreq(lbp_image)

    print(histogram)
    #print(histogram.shape);

    filename_out = str(i) + ".txt";
    file_out = open(DIR_OUT + filename_out, 'w')
    file_out.write(str(histogram));
    file_out.close();

    cv2.waitKey(500)
    cv2.destroyAllWindows()

#image = data.load('C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/spectrograms/55/1.png')

#print(lbp_image.shape)
#