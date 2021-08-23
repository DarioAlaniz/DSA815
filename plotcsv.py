import matplotlib.pyplot as plt
import numpy as np
from classCSV.extratCSV import extratCSV

'''
https://www.minicircuits.com/pdfs/QCN-13D+.pdf 
https://ar.mouser.com/datasheet/2/1030/EP2RCW_2b-1858382.pdf
https://www.minicircuits.com/pdfs/SYM-63LH+.pdf
_________Primera mediciones LO-IF (Respuesta mixer):
Con los mixer se tuvo en cuenta las peridas de los splitter 8,5dB EP2RCW(hoja de datos)
y splitter en cuadratura 4.0 dB QCN-13D+ (medidos!, en la hoja de datos era de 3.2 aprox)
Para ver la asilacion se hizo --» abs(salida - entradaAlMixer); entradaAlMixer = inputdBm-8.5-4.0
_________Aclaraciones:
No se tiene los .cv de 20dBm por que el generador no garantizaba salida cte con 20dBm para todas las frecuencias
_________Tareas:
Graficar RF-FI
Probar con los generadores usb en modo inverso en las 2 entradas
'''
#######################################
# tema          = 'Aislacion_entre_puertos_LO-IF'
##########LO-IF-Io1
# value         = ['10 dBm','15 dBm']
# outputPort    = 'Io1'
# numerosCsv    = 2
# path1         = "image_and_csv/csv/TRACE1:LO+IF+10DBM[500MHZ+1500MHZ].CSV"
# path2         = "image_and_csv/csv/TRACE1:LO+IF+15DBM[500MHZ+1500MHZ].CSV"
# tiltePlot     = 'Respuesta Mixer '+ outputPort
# path3 = "image_and_csv/csv/TRACE1:LO+IF+20DBM[500MHZ+1500MHZ].CSV" 

##########LO-IF-Io2
# value         = ['10 dBm','15 dBm']
# outputPort    = 'Io2'
# numerosCsv    = 2
# path1         = "image_and_csv/csv/TRACE1:LO+IF+I2+10DBM[500MHZ+1500MHZ].CSV"
# path2         = "image_and_csv/csv/TRACE1:LO+IF+I2+15DBM[500MHZ+1500MHZ].CSV"
# tiltePlot     = 'Respuesta Mixer '+ outputPort
# path3 = "image_and_csv/csv/TRACE1:LO+IF+I2+20DBM[500MHZ+1500MHZ].CSV"

############LO-IF-Q1
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Qo1'
# numerosCsv      = 2
# path1           = "image_and_csv/csv/TRACE1:LO+IF+Q1+10DBM[500MHZ+1500MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:LO+IF+Q1+15DBM[500MHZ+1500MHZ].CSV"
# tiltePlot       = 'Respuesta Mixer '+ outputPort

# path3 = "image_and_csv/csv/TRACE1:LO+IF+Q1+20DBM[500MHZ+1500MHZ].CSV"


############LO-IF-Q2
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Qo2'
# numerosCsv      = 2
# path1           = "image_and_csv/csv/TRACE1:LO+IF+Q2+10DBM[500MHZ+1500MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:LO+IF+Q2+15DBM[500MHZ+1500MHZ].CSV"
# tiltePlot       = 'Respuesta Mixer '+ outputPort

# path3         = "image_and_csv/csv/TRACE1:LO+IF+Q2+20DBM[500MHZ+1500MHZ].CSV"

######################################################################################################################
# tema            = 'Respuesta_Splitter'
############Respuesta Splitter Cos1
# value           = ['5 dBm','10 dBm','15 dBm']
# outputPort      = 'Cos1'
# numerosCsv      = 3
# path1           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+COS1+5DBM[675MHZ+1300MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+COS1+10DBM[675MHZ+1300MHZ].CSV"
# path3           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+15DBM[675MHZ+1300MHZ].CSV"

############Respuesta Splitter Sen 1
# value           = ['5 dBm','10 dBm','15 dBm']
# outputPort      = 'Sen1'
# numerosCsv      = 3
# path1           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+SEN1+5DBM[675MHZ+1300MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+SEN1+10DBM[675MHZ+1300MHZ].CSV"
# path3           = "image_and_csv/csv/TRACE1:RESPUESTASPLITTER+SEN1+15DBM[675MHZ+1300MHZ].CSV"


#######################################################################################
tema            = 'Aislacion_RF_IF'
############ Aislacion RF-IF-Io1
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Io1'
# numerosCsv      = 2
# path1           ="image_and_csv/csv/TRACE1:RF+IF+I1+10DBM[0MHZ+2000MHZ].CSV"
# path2           ="image_and_csv/csv/TRACE1:RF+IF+I1+15DBM[0MHZ+2000MHZ].CSV"

#######################################
############Aislacion RF-IF-Io2
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Io2'
# numerosCsv      = 2
# path1           ="image_and_csv/csv/TRACE1:RFQ+IF+I2+10DBM[0MHZ+2000MHZ].CSV"
# path2           ="image_and_csv/csv/TRACE1:RFQ+IF+I2+15DBM[0MHZ+2000MHZ].CSV"

#######################################
## Aislacion RF-IF-Qo1
value           = ['10 dBm','15 dBm']
outputPort      = 'Qo1'
numerosCsv      = 2
path1           ="image_and_csv/csv/TRACE1:RF+IF+Q1+10DBM[0MHZ+2000MHZ].CSV"
path2           ="image_and_csv/csv/TRACE1:RF+IF+Q1+15DBM[0MHZ+2000MHZ].CSV"

#######################################
## Aislacion RF-IF-Qo2
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
    Lo_If           = extratCSV(paths[i])
    frequency       = Lo_If.get_frequency()
    ##############
    # #Aislacion IO-IF
    # inputdBmMixer   = int(value[i].rsplit(' ')[0]) - 8.5 - 4.0
    # dBm             = np.abs(np.array(Lo_If.get_dBm()) - inputdBmMixer)
    ##############
    ##Aislacion RF-IF
    inputdBmMixer   = int(value[i].rsplit(' ')[0]) - 8.5 #tengo solo encuenta el spliter que divide la potencia
    dBm             = np.abs(np.array(Lo_If.get_dBm()) - inputdBmMixer)
    # dBm               = np.array(Lo_If.get_dBm())
    ##Spliter en cuadratura
    # dBm       = int(value[i].rsplit(' ')[0])- np.array(Lo_If.get_dBm()) 
    # atte      = np.mean(np.extract(np.array(dBm)<)#0,dBm))
    ###
    plt.plot(frequency,dBm,label=value[i])#'\n Atenuacion Promedio: ' + str(round(atte,3)))
    # print(np.mean(np.extract(np.abs(dBm))))
    plt.legend(title='Input({}) power [dBm]'.format('LO'))


plt.title(tilte);plt.xlabel('Frequency[Hz]');plt.ylabel('Isolation[dB]')
plt.grid(True)
plt.xlim(6*10**6,1.45*10**9)
plt.savefig('/home/dario/Documentos/funda/fiMediciones/DSA815/image_and_csv/image/{}.jpg'.format(tilte))
plt.show()