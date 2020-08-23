import pandas as pd
import numpy as np

total = list(range(1987, 2018))
meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
cont = 0

nc_file_0 = np.load('C:/Users/User/Downloads/github/media_jan_total.npy')
nc_file_0 = nc_file_0 * 0

for anos in total:  
    
    nc_ano = 'C:/Users/User/Downloads/github/media_%s_total.npy' % str(anos)
    nc_ano = np.load(nc_ano)

    nc_file_0 = nc_ano + nc_file_0
    
    cont = cont + 1
    
A = nc_file_0 / 31
    
item = pd.DataFrame(A)
nome = 'C:/Users/User/Downloads/github/media_anos_total.npy' 
np.save(nome, item)

