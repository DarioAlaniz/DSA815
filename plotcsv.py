import matplotlib.pyplot as plt
import numpy as np
from classCSV.extratCSV import extratCSV

'''
_________LO-IF
Con los mixer se tuvo en cuenta las peridas de los splitter 8,5dB EP2RCW(hoja de datos)
y splitter en cuadratura 5.5 dB QCN-13D+ (medidos, en la hoja de datos era de 3.2 aprox)
No se tiene los .cv de 20dBm por que el generador no garantizaba salida cte con 20dBm para todas las frecuencias
_Tareas:
Graficar RF-FI
Probar con los generadores usb en modo inverso en las 2 entradas
'''
#######################################
# ##LO-IF-Io1
# tema          = 'Aislacion_entre_puertos_LO-IF'
# value         = ['10 dBm','15 dBm']
# outputPort    = 'Io1'
# numerosCsv    = 2
# path1         = "image_and_csv/csv/TRACE1:LO+IF+10DBM[500MHZ+1500MHZ].CSV"
# path2         = "image_and_csv/csv/TRACE1:LO+IF+15DBM[500MHZ+1500MHZ].CSV"
# path3 = "image_and_csv/csv/TRACE1:LO+IF+20DBM[500MHZ+1500MHZ].CSV" 

#######################################
##LO-IF-Io2
# tema          = 'Aislacion_entre_puertos_LO-IF'
# value         = ['10 dBm','15 dBm']
# outputPort    = 'Io2'
# numerosCsv    = 2
# path1         = "image_and_csv/csv/TRACE1:LO+IF+I2+10DBM[500MHZ+1500MHZ].CSV"
# path2         = "image_and_csv/csv/TRACE1:LO+IF+I2+15DBM[500MHZ+1500MHZ].CSV"
# path3 = "image_and_csv/csv/TRACE1:LO+IF+I2+20DBM[500MHZ+1500MHZ].CSV"

#######################################
##LO-IF-Q1
# tema            = 'Aislacion_entre_puertos_LO-IF'
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Qo1'
# numerosCsv      = 2
# path1           = "image_and_csv/csv/TRACE1:LO+IF+Q1+10DBM[500MHZ+1500MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:LO+IF+Q1+15DBM[500MHZ+1500MHZ].CSV"
# path3 = "image_and_csv/csv/TRACE1:LO+IF+Q1+20DBM[500MHZ+1500MHZ].CSV"

#######################################
##LO-IF-Q2
# tema            = 'Aislacion_entre_puertos_LO-IF'
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Qo2'
# numerosCsv      = 2
# path1           = "image_and_csv/csv/TRACE1:LO+IF+Q2+10DBM[500MHZ+1500MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:LO+IF+Q2+15DBM[500MHZ+1500MHZ].CSV"
# path3         = "image_and_csv/csv/TRACE1:LO+IF+Q2+20DBM[500MHZ+1500MHZ].CSV"

#######################################
##Respuesta Splitter Cos1
# tema            = 'Respuesta_Splitter'
# value           = ['5 dBm','10 dBm','15 dBm']
# outputPort      = 'Cos1'
# numerosCsv      = 3
# path1           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+COS1+5DBM[675MHZ+1300MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+COS1+10DBM[675MHZ+1300MHZ].CSV"
# path3           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+15DBM[675MHZ+1300MHZ].CSV"

#######################################
##Respuesta Splitter Sen 1
# tema            = 'Respuesta_Splitter'
# value           = ['5 dBm','10 dBm','15 dBm']
# outputPort      = 'Sen1'
# numerosCsv      = 3
# path1           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+SEN1+5DBM[675MHZ+1300MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+SEN1+10DBM[675MHZ+1300MHZ].CSV"
# path3           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+SEN1+15DBM[675MHZ+1300MHZ].CSV"


#######################################
## Aislacion RF-IF-Io1
tema            = 'Aislacion_RF_IF'
value           = ['10 dBm','15 dBm']
outputPort      = 'Io1'
numerosCsv      = 2
path1           ="image_and_csv/csv/TRACE1:RF+IF+I1+10DBM[0MHZ+2000MHZ].CSV"
path2           ="image_and_csv/csv/TRACE1:RF+IF+I1+15DBM[0MHZ+2000MHZ].CSV"

#######################################
## Aislacion RF-IF-Io2
# tema            = 'Aislacion_RF_IF'
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Io2'
# numerosCsv      = 2
# path1           ="image_and_csv/csv/TRACE1:RFQ+IF+I2+10DBM[0MHZ+2000MHZ].CSV"
# path2           ="image_and_csv/csv/TRACE1:RFQ+IF+I2+15DBM[0MHZ+2000MHZ].CSV"

#######################################
## Aislacion RF-IF-Qo1
# tema            = 'Aislacion_RF_IF'
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Qo1'
# numerosCsv      = 2
# path1           ="image_and_csv/csv/TRACE1:RF+IF+Q1+10DBM[0MHZ+2000MHZ].CSV"
# path2           ="image_and_csv/csv/TRACE1:RF+IF+Q1+15DBM[0MHZ+2000MHZ].CSV"

#######################################
## Aislacion RF-IF-Qo2
# tema            = 'Aislacion_RF_IF'
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Qo2'
# numerosCsv      = 2
# path1           ="image_and_csv/csv/TRACE1:RFQ+IF+Q2+10DBM[0MHZ+2000MHZ].CSV"
# path2           ="image_and_csv/csv/TRACE1:RFQ+IF+Q2+10DBM[0MHZ+2000MHZ].CSV"



paths       = [path1,path2]
# paths       = [path1,path2,path3]
placa       = 'Placa1'
tilte       ='{}_{}_{}'.format(tema,outputPort,placa)

plt.figure(tema)
for i in range(numerosCsv):
    Lo_If       = extratCSV(paths[i])
    frequency   = Lo_If.get_frequency()
    dBm         = np.abs(Lo_If.get_dBm())
    # dBm         = np.abs(Lo_If.get_dBm())-8.5-.4 #Resta de atenuacion en los spliter
    ##Spliter en cuadratura
    # dBm       = int(value[i].rsplit(' ')[0])- np.array(Lo_If.get_dBm()) 
    # atte      = np.mean(np.extract(np.array(dBm)<)#0,dBm))
    ###
    plt.plot(frequency,dBm,label=value[i])#'\n Atenuacion Promedio: ' + str(round(atte,3)))
    # print(np.mean(np.extract(np.abs(dBm))))
    plt.legend(title='Input power [dBm]')


plt.title(tilte);plt.xlabel('Frequency[Hz]');plt.ylabel('Loss[dBm]')
plt.grid(True)
# plt.xlim(0.7*10**9,1.3*10**9)
plt.savefig('/home/dario/Documentos/funda/fiMediciones/DSA815/image_and_csv/image/{}.jpg'.format(tilte))
plt.show()