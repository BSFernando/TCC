import pandas as pd
import numpy as np
import netCDF4 as n4

anos = list(range(1987, 2018))
meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
lista_meses1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

nc_file_0 = 'C:/Users/User/sst.day.mean.1987.nc'     
sst_0 = n4.Dataset(nc_file_0)
sst_0 = sst_0.variables['sst'][0,:,:]
sst_0 = sst_0 * 0

contador = 0
contador1 = 1
      
while contador < len(meses):                                        
        
    for v in anos:    
        
        nc_file = 'C:/Users/User/sst.day.mean.%s.nc' % str(v)
        ano_data = n4.Dataset(nc_file)
        cont_dia = lista_meses1[contador]
        cont_dia_1 = 0
        sstf = sst_0 * 0

        while cont_dia < lista_meses1[contador1]:
            sst = ano_data.variables['sst'][cont_dia,:,:]
            sstf = sst + sstf
            cont_dia = cont_dia + 1
            cont_dia_1 = cont_dia_1 + 1
    
        sstf = sstf/cont_dia_1
        sstf = pd.DataFrame(sstf)
        np.save(('C:/Users/User/media_%s_%s.npy' % (str(meses[contador]), str(v))), sstf)
    
    contador = contador + 1
    contador1 = contador1 + 1    
