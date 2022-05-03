### ipython move_sources.py folder_name
# Helper script
# Splits data based on observing target
import glob
import os
from astropy.io import fits
import shutil  
import sys

os.chdir(sys.argv[1])

def move(lst, location):
    for source in lst:
        shutil.move(source, location)
    print('Done moving to', location)


g7 = []
tycho = []
ctb109 = []
flat = []
bias = []
#ic1396 = []

names = sorted(glob.glob('r*fit'))

#print(names)

for i in names:
#    print(i)
    if (fits.open(i)[0].header['OBJECT'])[:6] == 'CTB109':
        ctb109.append(i)
print('CTB109',ctb109)


for i in names:
    if (fits.open(i)[0].header['OBJECT'])[:5] == 'Tycho':
        tycho.append(i)
print('Tycho',tycho)

for i in names:
    if (fits.open(i)[0].header['OBJECT'])[:2] == 'G7' or (fits.open(i)[0].header['OBJECT'])[:2] == 'g7':
        g7.append(i)
print('G7',g7)

#for i in names:
#    if (fits.open(i)[0].header['OBJECT'])[:6] == 'IC1396':
#        ic1396.append(i)
#print('IC1396',ic1396)

for i in names:
    if (fits.open(i)[0].header['OBJECT'])[:3] == 'Sky' or (fits.open(i)[0].header['OBJECT'])[:4] == 'Flat':
        flat.append(i)
print('Flats',flat)

for i in names:
    if (fits.open(i)[0].header['OBJECT'])[:4] == 'Bias':
        bias.append(i)
print('Bias',bias)

directory_list = ['flats', 'bias', 'g7', 'ctb109', 'tycho'] #, 'ic1396']

for directory in directory_list:
	if not os.path.exists(directory):
		os.makedirs(directory)

move(ctb109,'./ctb109')
move(tycho,'./tycho')
move(g7,'./g7')
#move(ic1396,'./ic1396')
move(flat,'./flats')
move(bias,'./bias')


names2 = glob.glob('r*fit')
print('Leftover files')
for i in names2:
    print(i,fits.open(i)[0].header['OBJECT'])
