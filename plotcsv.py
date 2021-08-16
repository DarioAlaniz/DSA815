import matplotlib.pyplot as plt
import numpy as np
from classCSV.extratCSV import extratCSV

'''
Graficar Aislacion, solo con los mixer
Restar las perdidas de los splitter 8,5dB EP2RCW
y splitter en cuadratura 5dB
Graficar RF-FI
Probar con los generadores usb en modo inverso en las 2 entradas
'''
#######################################
# ##LO-IF-Io1
# path1 = "image_and_csv/csv/TRACE1:LO+IF+10DBM[500MHZ+1500MHZ].CSV"
# path2 = "image_and_csv/csv/TRACE1:LO+IF+15DBM[500MHZ+1500MHZ].CSV"
# path3 = "image_and_csv/csv/TRACE1:LO+IF+20DBM[500MHZ+1500MHZ].CSV"

#######################################
##LO-IF-Io2
# path1 = "image_and_csv/csv/TRACE1:LO+IF+I2+10DBM[500MHZ+1500MHZ].CSV"
# path2 = "image_and_csv/csv/TRACE1:LO+IF+I2+15DBM[500MHZ+1500MHZ].CSV"
# path3 = "image_and_csv/csv/TRACE1:LO+IF+I2+20DBM[500MHZ+1500MHZ].CSV"

#######################################
##LO-IF-Q1
# path1 = "image_and_csv/csv/TRACE1:LO+IF+Q1+10DBM[500MHZ+1500MHZ].CSV"
# path2 = "image_and_csv/csv/TRACE1:LO+IF+Q1+15DBM[500MHZ+1500MHZ].CSV"
# path3 = "image_and_csv/csv/TRACE1:LO+IF+Q1+20DBM[500MHZ+1500MHZ].CSV"

#######################################
##LO-IF-Q2
# path1       = "image_and_csv/csv/TRACE1:LO+IF+Q2+10DBM[500MHZ+1500MHZ].CSV"
# path2       = "image_and_csv/csv/TRACE1:LO+IF+Q2+15DBM[500MHZ+1500MHZ].CSV"
# path3       = "image_and_csv/csv/TRACE1:LO+IF+Q2+20DBM[500MHZ+1500MHZ].CSV"

#######################################
##Respuesta Splitter
pwd="./image_and_csv/csv"

path1       = f"{pwd}/TRACE1:LO+IF+10DBM[500MHZ+1500MHZ].CSV"
path2       = f"{pwd}/TRACE1:LO+IF+15DBM[500MHZ+1500MHZ].CSV"
path3       = f"{pwd}/TRACE1:LO+IF+20DBM[500MHZ+1500MHZ].CSV"

paths       = [path1,path2,path3]
outputPort  = 'Io1'
placa       = 'Placa1'
tema        = "Aislacion#entre#puertos#LO/IF"
value       = ['5','10','15']

tilte       ='{}#{}#{}'.format(tema,outputPort,placa)

plt.figure(1)
for i in range(3):
    Lo_If       = extratCSV(paths[i])
    frequency   = Lo_If.get_frequency()
    dBm         = Lo_If.get_dBm()
    # plt.figure(1)
    # promedio = np.mean(np.extract(np.array(dBm)>-10,dBm))
    # print(promedio)
    plt.plot(frequency,np.abs(np.array(dBm)-int(value[i])),label=value[i])
    # print(np.mean(np.extract(np.abs(dBm))))
    plt.legend(title='Input power [dBm]')


plt.title(tilte);plt.xlabel('Frequency[Hz]');plt.ylabel('Magnitud[dBm]')
plt.grid(True)
plt.xlim(0.6*10**9,1.35*10**9)
plt.savefig('{}.jpg'.format(tilte))
print(tilte)
plt.show()