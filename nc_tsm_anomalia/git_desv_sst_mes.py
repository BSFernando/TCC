import numpy as np

total = list(range(1987, 2018))
meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for mes in meses:
    
    nc_file_0 = np.load('C:/Users/User/Downloads/github/media_jan_total.npy')
    nc_file_0 = nc_file_0 * 0
    
    for anos in total:  
        
        nc_mes_ano = 'C:/Users/User/Downloads/github/media_%s_%s.npy' % (str(mes), str(anos))
        nc_mes_ano = np.load(nc_mes_ano)
        nc_mes_total = 'C:/Users/User/Downloads/github/media_%s_total.npy' % str(mes)
        nc_mes_total = np.load(nc_mes_total)

        somatorio = (nc_mes_ano - nc_mes_total) ** 2
        nc_file_0 = somatorio + nc_file_0
        
    nc_file_0 = ((nc_file_0/31) ** (1/2))

    nome = 'C:/Users/User/Downloads/github/desv_%s.npy' % str(mes)
    np.save(nome, nc_file_0)

