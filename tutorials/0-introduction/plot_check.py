from pykoala.data_container import RSS
import os
from pykoala.instruments.koala_ifu import koala_rss
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

data_path = 'tutorials/data/koala/'
single_fits_sample = '385R/27feb20028red.fits'
file_sample = os.path.join(data_path, single_fits_sample)
rss_sample = koala_rss(file_sample)

rss_sample.plot_rss_image()
plt.show()
