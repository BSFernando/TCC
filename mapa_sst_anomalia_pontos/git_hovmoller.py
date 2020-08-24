import pandas as pd
import numpy as np
import os
os.environ['PROJ_LIB'] = r'C:\Users\User\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'    
import matplotlib.pyplot as plt

total = list(range(1987, 2018))
meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

lista = []
    
for ano in total:
    
    file = np.load('C:/Users/User/Downloads/github/anomalia_%s_total.npy' % str(ano))
    file = file[::-1]
    file = file[188:208,1180:1220]
    file = file[::-1]
    file = pd.DataFrame(file)
    file = file.mean()
    file = pd.DataFrame(file)
    file = file.transpose()
    lista.append(file)
    

aaa = pd.concat(lista)        
ppp = plt.figure(figsize = (25, 40))
ppp.subplots_adjust(hspace = 0)

uuu = plt.imshow(aaa, cmap='jet', aspect='auto', interpolation = 'bilinear')
plt.yticks(range(0,32, 5), labels = ("1987","1992", "1997", "2002", "2007", "2012", "2017"), size = 100)
plt.xticks(range(10, 40 , 10), labels = ('62.5W', '60.0W', '57.5W'), size = 100)
plt.tick_params(labelsize=50, pad = 15) 
plt.colorbar(uuu, spacing = "proportinal", orientation='horizontal', aspect=25, shrink=.7, pad = 0.05).ax.tick_params(labelsize=50)
plt.grid()
