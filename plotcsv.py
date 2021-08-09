import matplotlib.pyplot as plt
import numpy as np
from classCSV.extratCSV import extratCSV

path1 = "../image_and_csv/TRACE1:LO+IF+10DBM[500MHZ+1500MHZ].CSV"
path2 = "../image_and_csv/TRACE1:LO+IF+15DBM[500MHZ+1500MHZ].CSV"
path3 = "../image_and_csv/TRACE1:LO+IF+20DBM[500MHZ+1500MHZ].CSV"

paths = [path1,path2,path3]
value = ['10dBm','15dBM','20dBm']

plt.figure(1)
for i in range(3):
    Lo_If = extratCSV(paths[i])
    frequency = Lo_If.get_frequency()
    dBm = Lo_If.get_dBm()
    # plt.figure(1)
    plt.plot(frequency,dBm,label=value[i]);plt.legend()
tilte='Aislacion_entre_Puertos_LO-IF'
plt.title(tilte);plt.xlabel('Frequency[Hz]');plt.ylabel('Magnitud[dBm]')
plt.grid()
plt.savefig('/home/dario/Documentos/funda/fiMediciones/DSA815/image_and_csv/image/{}.jpg'.format(tilte))
plt.show()

