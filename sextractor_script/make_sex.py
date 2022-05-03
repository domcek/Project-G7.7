# ipython make_sex.py science_folder_path
# Runs sextractor on all files
import glob
import os
import sys
import matplotlib.pyplot as plt
import numpy as np


work_dir_path = sys.argv[1]
print('Working in directory:', work_dir_path)

names = sorted(glob.glob(work_dir_path + 'r*fit'))
print('There are ' + str(len(names)) + ' files in the folder')

if os.path.exists(work_dir_path + '/sextractor') == False:
    os.mkdir(work_dir_path + '/sextractor')

counter = 0
for file in names:
    counter += 1
    name = file.split('/')[-1][:-4]
    print(counter, '/', len(names), name)
    os.system('sextractor ' + file + ' -c default.sex -CATALOG_NAME ' + work_dir_path + 'sextractor/' + name + 'sex.dat' )

print('Done')
