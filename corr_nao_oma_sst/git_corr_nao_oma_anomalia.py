import pandas as pd
import numpy as np
import os
os.environ['PROJ_LIB'] = r'C:\Users\User\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'    
import matplotlib.pyplot as plt
import time
from statsmodels.tsa.filters import hp_filter

start = time.time()

tabela = pd.read_excel("C:/Users/User/Downloads/github/tabela_meses_anomalia_nao_oma.xlsx")
tabela = pd.DataFrame(tabela)

datas = list(range(-2017, -1986,1)) + list(range(1986, 2018,1))
sup = 1.96/np.sqrt(372)
inf = (1.96/np.sqrt(372))*-1


plt.figure(figsize = (40,10))
auto5 = np.correlate(tabela['Media'], tabela["OMA"], mode = 'full')
auto5 = auto5/auto5.max()
auto5 = auto5[auto5.size//2:]
oma_media = hp_filter.hpfilter(auto5,129600)
plt.plot(auto5)
plt.plot(oma_media[1], label = "HP Filter", c = "grey", linewidth = 10)
plt.axhline(inf, color="grey", lw = 5, linestyle = "--")
plt.axhline(sup, color="grey", lw = 5, linestyle = "--")
plt.axhline(y=0, color="black", lw = 2)
t = plt.stem(auto5, linefmt = "-", markerfmt='none', use_line_collection = True)
plt.setp(t, color = "k")
plt.xticks(range(0,373,12), labels = list(range(0, 32, 1)), size = 30)
plt.yticks(np.arange(-1,1.1,0.5), size = 30)
plt.grid()
plt.legend(loc = 2, fontsize = 20)



plt.figure(figsize = (40,10))
auto6 = np.correlate(tabela['Media'], tabela["NAO"], mode = 'full')
auto6 = auto6/auto6.max()
auto6 = auto6[auto6.size//2:]
nao_media = hp_filter.hpfilter(auto6,129600)
plt.plot(auto6, c = "k")
plt.plot(nao_media[1], label = "HP Filter", c = "grey", linewidth = 10)
plt.axhline(inf, color="grey", lw = 5, linestyle = "--")
plt.axhline(sup, color="grey", lw = 5, linestyle = "--")
plt.axhline(y=0, color="black", lw = 2)
t = plt.stem(auto6, linefmt = "-", markerfmt='none', use_line_collection = True)
plt.setp(t, color = "k")
plt.xticks(range(0,373,12), labels = list(range(0, 32, 1)), size = 30)
plt.yticks(np.arange(-1,1.1,0.5), size = 30)
plt.grid()
plt.legend(loc = 2, fontsize = 20)

oma_f = hp_filter.hpfilter(tabela["OMA"],129600)
nao_f = hp_filter.hpfilter(tabela["NAO"],129600)
media_f = hp_filter.hpfilter(tabela["Media"],129600)


a = plt.figure(figsize = (45,18))
a.add_subplot(3,1,1)
plt.plot(tabela["Media"]/tabela["Media"].max(), label = "SST Anomaly", c = "k")
plt.plot(media_f[1]/media_f[1].max(), label = "HP filter", c = "grey", linewidth = 10)
plt.yticks(np.arange(-1,1.1,0.5), size = 30)
plt.xticks(range(0,373,12), labels = [], size = 30, rotation = 45)
plt.legend(fontsize = 20, loc = 2)
a.add_subplot(3,1,2)
plt.plot(tabela["OMA"]/tabela["OMA"].max(), label = "AMO", c = "k")
plt.plot(oma_f[1]/oma_f[1].max(), label = "HP filter", c = "grey", linewidth = 10)
plt.yticks(np.arange(-1,1.1,0.5), size = 30)
plt.xticks(range(0,373,12), labels = [], size = 30, rotation = 45)
plt.legend(fontsize = 20, loc = 2)
a.add_subplot(3,1,3)
plt.plot(tabela["NAO"]/(-1* tabela["NAO"].min()), label = "NAO", c = "k")
plt.plot(nao_f[1]/nao_f[1].max(), label = "HP filter", c = "grey", linewidth = 10)
plt.yticks(np.arange(-1,1.1,0.5), size = 30)
plt.xticks(range(0,373,12), labels = list(range(1987, 2018,1)), size = 30, rotation = 45)
plt.legend(fontsize = 20, loc = 2)
