import pandas as pd
import numpy as np

total = list(range(1987, 2018))
meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for mes in meses:
    
    nc_file_0 = np.load('C:/Users/User/media_jan_total.npy')
    nc_file_0 = nc_file_0 * 0
    
    for anos in total:
        
        nc_mes_ano = 'C:/Users/User/media_%s_%s.npy' % (str(mes), str(anos))
        nc_mes_ano = np.load(nc_mes_ano)
        
        nc_mes_total = 'C:/Users/User/media_%s_total.npy' % str(mes)
        nc_mes_total = np.load(nc_mes_total)

        nc_desv = 'C:/Users/User/desv_%s.npy' % str(mes)
        nc_desv = np.load(nc_desv)
    
        anom_norm = (nc_mes_ano - nc_mes_total) / nc_desv
                        
        anom_norm = pd.DataFrame(anom_norm)
        nome = 'C:/Users/User/anomalia_%s_%s.npy' % (str(mes), str(anos))
        np.save(nome, anom_norm)
