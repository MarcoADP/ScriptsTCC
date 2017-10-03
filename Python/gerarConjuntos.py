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

LBPName = 'lbp' + str(LBPNeighbors) + str(LBPRadius)

DIR = 'C:/Users/smarttcon-dev00/Google Drive/TCC/Base Final/' + LBPName + '/'+ db + '/'

size_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(os.listdir(DIR))
print (size_files)
for i in range(1, size_files):
    print(i);
    filename = str(i) + ".txt";