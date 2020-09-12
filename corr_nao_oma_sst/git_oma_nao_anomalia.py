import pandas as pd
import numpy as np

tabela = {}
tabela = pd.DataFrame(tabela)

total = list(range(1987, 2018))
meses = ['jan','fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

oma = np.loadtxt('C:/amo.txt')
oma = pd.DataFrame(oma)
oma.index = oma[0]
oma = oma.drop(columns = 0)
oma = oma[(oma.index > 1986) & (oma.index < 2018)]
oma.columns = meses

nao = np.loadtxt('C:/norm.nao.monthly.txt')
nao = pd.DataFrame(nao)
nao.index = nao[0]
nao = nao.drop(columns = 0)
nao = nao[(nao.index > 1986) & (nao.index < 2018)]
nao.columns = meses

z = 0
  
for ano in total:
    
    for mes in meses:
    
        file = np.load('C:/anomalia_%s_%s.npy' % (str(mes), str(ano)))
        file = file[::-1]
        file = file[188:208,1180:1220]
        file = file[::-1]
        file = pd.DataFrame(file)
        media = np.array(file)
        media = media.mean()
        
        tabela.loc[z, 'Media'] = media
        tabela.loc[z, 'Data'] = str(ano) + " " + str(mes)
        tabela.loc[z,"NAO"] = nao[mes][ano]
        tabela.loc[z,"OMA"] = oma[mes][ano]
        
        z = z + 1

tabela.to_excel("C:/tabela_meses_anomalia_nao_oma.xlsx")
  
