import pandas as pd
import numpy as np
import scipy.cluster.vq as sc
import os
os.environ['PROJ_LIB'] = r'C:\Users\User\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'    
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

tabela = pd.ExcelFile('C:/Users/User/Documents/Coisas/Sharknado 3,o TCC/87_17.xlsx')

tab1 = tabela.parse('Anos')
tab1['ReLenCM'].fillna(((tab1['ReWgtKG'] / 0.00068) ** 0.458), inplace = True)
tab1['ReWgtKG'].fillna(((tab1['ReLenCM'] ** 2.18) * 0.00068), inplace = True)
tab2 = tab1.drop(columns = ['RcYear', 'RcDate', 'RcLatY', 'RcLonX', 'RcLenCM', 'RcWgtKG'])
tab2.isnull().sum()
tab6 = tab2[(tab2['ReLatY'] > 34) & (tab2['ReLatY'] < 51) & (tab2['ReLonX'] < -30)]
ano_escolhido = tab6.groupby('ReYear')

total_esc = [1987, 1993, 1999, 2006, 2011, 2017]
cont = 0

grade = plt.figure(figsize = (18,8.5))
grade.subplots_adjust(hspace = 0)

for ano in total_esc:
    
    file = np.load('C:/Users/User/Downloads/github/media_%s_total.npy' % str(ano))
    file = file[::-1]
    file = file[160:240,1120:1280]
    file = file[::-1]
    long = list(np.arange(-79.875,-40,0.25))
    lat = list(np.arange(30.125,50,0.25))
    
    grade.add_subplot(2,3,cont+1)
    
    fig = Basemap( llcrnrlon=-80,llcrnrlat=30,urcrnrlon=-40,urcrnrlat=50, resolution='l', lon_0 = -60, lat_0= 37.5)
    sst = fig.imshow(file, cmap="jet", interpolation = 'bilinear', aspect='auto')
    fig.drawcoastlines()
    fig.fillcontinents(color='0.8',lake_color='white') 
    fig.drawparallels(np.arange(-90.,91.,10.),labels=[1,0,0,0], size = 20)
    fig.drawmeridians(np.arange(-180.,181.,15.),labels=[0,0,0,1], size = 20)
    long_1, lat_1 = fig(*np.meshgrid(long, lat))
    contorno = fig.contour(long_1, lat_1, data = file, colors = 'k',linewidths = 0.5)
    plt.clabel(contorno, inline = True, fontsize=10, fmt='% 4d')
    
    tab = {'lat' : ano_escolhido.get_group(ano)['ReLatY'], 'log' : ano_escolhido.get_group(ano)['ReLonX']}
    tab = pd.DataFrame(tab)
    clust = sc.kmeans(tab, 1)
    
    fig.scatter(x = list(tab['log']), y = list(tab['lat']), marker = 'o', c = 'pink', latlon=True, s = 60, edgecolors = 'k')
    fig.scatter(clust[0][0][1],clust[0][0][0], c = 'k',  marker = 'P', latlon=True, s = 350, edgecolors = 'w')
    plt.title(ano, size = 20)
    cont = cont + 1

bar_ax = grade.add_axes([0.3, 0.1, 0.42, 0.02])
grade.colorbar(sst, cax = bar_ax, orientation = "horizontal").ax.tick_params(labelsize=20)
