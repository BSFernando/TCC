import pandas as pd
import numpy as np

total = list(range(1987, 2018))
meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for anos in total:
    
    nc_ano = 'C:/Users/User/Downloads/github/media_%s_total.npy' % str(anos)
    nc_ano = np.load(nc_ano)
    
    nc_ano_total = 'C:/Users/User/Downloads/github/media_anos_total.npy' 
    nc_ano_total = np.load(nc_ano_total)

    nc_desv = 'C:/Users/User/Downloads/github/desv_anos_total.npy'
    nc_desv = np.load(nc_desv)

            
    anom_norm = (nc_ano - nc_ano_total) / nc_desv
                
    anom_norm = pd.DataFrame(anom_norm)
    nome = 'C:/Users/User/Downloads/github/anomalia_%s_total.npy' % str(anos)
    np.save(nome, anom_norm)
