import pandas as pd
import numpy as np
import scipy.cluster.vq as sc
import os
os.environ['PROJ_LIB'] = r'C:\Users\User\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'    
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

tabela = pd.ExcelFile('C:/Users/User/banco_de_dados.xlsx')

tab1 = tabela.parse('Anos')
tab1['ReLenCM'].fillna(((tab1['ReWgtKG'] / 0.00068) ** 0.458), inplace = True)
tab1['ReWgtKG'].fillna(((tab1['ReLenCM'] ** 2.18) * 0.00068), inplace = True)
tab2 = tab1.drop(columns = ['RcYear', 'RcDate', 'RcLatY', 'RcLonX', 'RcLenCM', 'RcWgtKG'])
tab2.isnull().sum()
tab6 = tab2[(tab2['ReLatY'] > 34) & (tab2['ReLatY'] < 51) & (tab2['ReLonX'] < -30)]
ano_escolhido = tab6.groupby('ReYear')

cont = 0
ano = 1987

grade = plt.figure(figsize = (20,24))
grade.subplots_adjust(hspace = 0)

while ano < 2018:
    
    file = np.load('C:/Users/User/media_%s_total.npy' % str(ano))
    file = file[::-1]
    file = file[160:240,1120:1280]
    file = file[::-1]

    grade.add_subplot(8,4,cont+1)
    
    fig = Basemap( llcrnrlon=-80,llcrnrlat=30,urcrnrlon=-40,urcrnrlat=50, resolution='l', lon_0 = -60, lat_0= 37.5)
    sst = fig.imshow(file, cmap="jet", interpolation = 'bilinear', aspect='auto')
    fig.drawcoastlines()
    fig.fillcontinents(color='0.8',lake_color='white') 
    fig.drawparallels(np.arange(-90.,91.,10.),labels=[1,0,0,0], size = 10)
    fig.drawmeridians(np.arange(-180.,181.,15.),labels=[0,0,0,1], size = 10)

    for ano_tab,dados_ano in ano_escolhido:
        if ano_tab == ano:
            tab = {'lat' : ano_escolhido.get_group(ano)['ReLatY'], 'log' : ano_escolhido.get_group(ano)['ReLonX']}
            tab = pd.DataFrame(tab)
            clust = sc.kmeans(tab, 1)
            
            fig.scatter(x = list(tab['log']), y = list(tab['lat']), marker = 'o', c = 'pink', latlon=True, s = 40, edgecolors = 'k')
            fig.scatter(clust[0][0][1],clust[0][0][0], c = 'k',  marker = 'X', latlon=True, s = 250, edgecolors = 'w')
            plt.title(ano, size = 10)        
            break
        else:
            pass
    cont = cont + 1
    ano = ano + 1

cbar_ax = grade.add_axes([0.3, 0.11, 0.42, 0.012])
grade.colorbar(sst, cax = cbar_ax, orientation = "horizontal").ax.tick_params(labelsize=15)
