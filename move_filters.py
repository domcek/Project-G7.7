### ipython move_filters.py folder_name
# Helper script
# Splits data based on the filter
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


ha = []
hb = []
o3 = []
s2 = []
r = []
g = []

directory_list = ['ha', 'hb', 'o3', 's2', 'r', 'g']

for directory in directory_list:
        if not os.path.exists(directory):
                os.makedirs(directory)

names = sorted(glob.glob('r*fit'))

print(names)

for i in names:
    if (fits.open(i)[0].header['WFFBAND']) == 'Halpha':
        ha.append(i)
print('Halpha',ha)


for i in names:
    if (fits.open(i)[0].header['WFFBAND'])[:5] == 'Hbeta':
        hb.append(i)
print('Hbeta',hb)

for i in names:
    if (fits.open(i)[0].header['WFFBAND'])[:1] == 'g':
        g.append(i)
print('g',g)

for i in names:
    if (fits.open(i)[0].header['WFFBAND'])[:1] == 'r':
        r.append(i)
print('r',r)

for i in names:
    if (fits.open(i)[0].header['WFFBAND'])[:5] == '[SII]':
        s2.append(i)
print('SII', s2)

for i in names:
    if (fits.open(i)[0].header['WFFBAND'])[:6] == '[OIII]':
        o3.append(i)
print('OIII', o3)

move(ha,'./ha')
move(hb,'./hb')
move(g,'./g')
move(r,'./r')
move(s2,'./s2')
move(o3,'./o3')

names2 = glob.glob('r*fit')
print('Leftover files')
for i in names2:
    print(i,fits.open(i)[0].header['OBJECT'])
