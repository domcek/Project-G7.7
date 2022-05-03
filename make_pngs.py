# Make a PNG file from all chips of the detector

from astropy.io import fits
from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import platform
import glob
import os
import sys
from astropy.visualization import (MinMaxInterval, ZScaleInterval, SqrtStretch, ImageNormalize)


int_raw_data_path = '/media/vdomcek/Storage/work/2019_INT_La_Palma/'
work_dir_path = int_raw_data_path + sys.argv[1]
print('Working in directory:', work_dir_path)
if os.path.exists(work_dir_path + '/png') == False:
    os.mkdir(work_dir_path + '/png')

names = sorted(glob.glob(work_dir_path + '/r*fit'))
print('There are ' + str(len(names)) + ' files in the folder')

counter = 0
for file in names:
    counter += 1
    png_name = file.split('/')[-1][:-3]
    print(counter,'/', len(names), png_name)
    hdr = fits.open(file)
    
    fig = plt.figure(1, figsize=(10,10), dpi=300)
    plt.subplots_adjust(wspace=0.)


    ax0 = plt.subplot(141) 
    ax0.set_title(png_name[:-1]+'\n Chip 0')
    im = ax0.imshow(hdr[1].data, cmap='Greys', origin='lower', norm=ImageNormalize(hdr[1].data, ZScaleInterval()))
    # cbar = fig.colorbar(im) 
    # cbar.set_label(r'Flux density [Jy]', rotation=270,size=25,labelpad=26)

    ax1 = plt.subplot(142) #, projection=WCS(hdu_radio_4_72Ghz_bin3.header))
    ax1.set_title('Chip 1')
    im = ax1.imshow(hdr[2].data, cmap='Greys', origin='lower', norm=ImageNormalize(hdr[2].data, ZScaleInterval()))
    # cbar = fig.colorbar(im) 
    # cbar.set_label(r'Flux density [Jy]', rotation=270,size=25,labelpad=26)
    ax1.tick_params(
        axis='y',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        left=True,      # ticks along the bottom edge are off
        labelleft=False)

    ax2 = plt.subplot(143) 
    ax2.set_title('Chip 2')
    im = ax2.imshow(hdr[3].data, cmap='Greys', origin='lower', norm=ImageNormalize(hdr[3].data, ZScaleInterval()))
    # cbar = fig.colorbar(im) 
    # cbar.set_label(r'Flux density [Jy]', rotation=270,size=25,labelpad=26)
    ax2.tick_params(
        axis='y',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        left=True,      # ticks along the bottom edge are off
        labelleft=False)

    ax3 = plt.subplot(144) 
    ax3.set_title('Chip 3')
    im = ax3.imshow(hdr[4].data, cmap='Greys', origin='lower', norm=ImageNormalize(hdr[4].data, ZScaleInterval()))
    # cbar = fig.colorbar(im) 
    # cbar.set_label(r'Flux density [Jy]', rotation=270,size=25,labelpad=26)
    ax3.tick_params(
        axis='y',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        left=True,      # ticks along the bottom edge are off
        labelleft=False)

    plt.savefig(work_dir_path + '/png/' + png_name + 'png', bbox_inches='tight' )
    hdr.close()
    fig.clf()
