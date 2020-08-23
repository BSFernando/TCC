import pandas as pd
import numpy as np
import netCDF4 as n4

anos = list(range(1987, 2018))
nome = 'C:/Users/User/Downloads/tcc/mapas/.nc/sst.day.mean.1987.nc'     
sst_0 = n4.Dataset(nome)
sst_0 = sst_0.variables['sst'][0,:,:]
sst_0 = sst_0 * 0
      
for v in anos:
    
    sstf = sst_0 * 0
    contador = 0
    
    nc_file = 'C:/Users/User/Downloads/tcc/mapas/.nc/sst.day.mean.%s.nc' % str(v)
    ano_data = n4.Dataset(nc_file)
    data = ano_data.variables['time']

    while contador < len(data):
        
        sst = ano_data.variables['sst'][contador,:,:]
        sstf = sst + sstf
        contador = contador + 1
        
    sstf = sstf/len(data)
    sstf = pd.DataFrame(sstf)
    np.save(('C:/Users/User/Downloads/github/media_%s_total.npy' % str(v)), sstf)
