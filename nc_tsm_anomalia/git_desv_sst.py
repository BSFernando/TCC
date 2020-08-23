import pandas as pd
import numpy as np

total = list(range(1987, 2018))
meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    
nc_file_0 = np.load('C:/Users/User/Downloads/github/media_jan_total.npy')
nc_file_0 = nc_file_0 * 0

for anos in total:  
    
    nc_ano = 'C:/Users/User/Downloads/github/media_%s_total.npy' % str(anos)
    nc_ano = np.load(nc_ano)
    nc_ano_media = 'C:/Users/User/Downloads/github/media_anos_total.npy'
    nc_ano_media = np.load(nc_ano_media)

    somatorio = (nc_ano - nc_ano_media) ** 2
    nc_file_0 = somatorio + nc_file_0
    
E = ((nc_file_0/31) ** (1/2))
    
item = pd.DataFrame(E)
nome = 'C:/Users/User/Downloads/github/desv_anos_total.npy' 
np.save(nome, item)

