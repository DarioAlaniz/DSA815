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
Graficar RF-FI con los nuevos datos extraidos
Probar con los generadores usb en modo inverso en las 2 entradas
Consultar a lean, sobre los armonicos como armar los plots

'''
#######################################
# tema          = 'Aislacion_entre_puertos_LO-IF'
##########LO-IF-Io1
# value         = ['10 dBm','13 dBm']
# outputPort    = 'Io1'
# numerosCsv    = 2
# path1         = "image_and_csv/csv/TRACE1:LO+IF+10DBM[500MHZ+1500MHZ].CSV"
# path2         = "image_and_csv/csv/TRACE1:LO+IF+I1+13DBM[600MHZ+1500MHZ].CSV"
# tiltePlot     = 'Respuesta Mixer '+ outputPort

##########LO-IF-Io2
# value         = ['10 dBm','13 dBm']
# outputPort    = 'Io2'
# numerosCsv    = 2
# path1         = "image_and_csv/csv/TRACE1:LO+IF+I2+10DBM[500MHZ+1500MHZ].CSV"
# path2         = "image_and_csv/csv/TRACE1:LO+IF+I2+13DBM[675MHZ+1500MHZ].CSV"
# tiltePlot     = 'Respuesta Mixer '+ outputPort

############LO-IF-Q1
# value           = ['10 dBm','13 dBm']
# outputPort      = 'Qo1'
# numerosCsv      = 2
# path1           = "image_and_csv/csv/TRACE1:LO+IF+Q1+10DBM[675MHZ+1500MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:LO+IF+Q1+13DBM[675MHZ+1500MHZ].CSV"
# tiltePlot       = 'Respuesta Mixer '+ outputPort

###########LO-IF-Q2
# value           = ['10 dBm','13 dBm']
# outputPort      = 'Qo2'
# numerosCsv      = 2
# path1           = "image_and_csv/csv/TRACE1:LO+IF+Q2+10DBM[675MHZ+1500MHZ].CSV"
# path2           = "image_and_csv/csv/TRACE1:LO+IF+Q2+13DBM[675MHZ+1500MHZ].CSV"
# tiltePlot       = 'Respuesta Mixer '+ outputPort

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
# tema            =tema + "_Armonicos_De_Salida"
############ Aislacion RF-IF-Io1 Armonicos
value           = ['13 dBm']
inFrequency     = ['100Mhz','300Mhz','400Mhz','500Mhz','1000Mhz']
outputPort      = 'Io1'
numerosCsv      = 5
path1           ="image_and_csv/csv/RF_IF/TRACE1:AISLACION+RF+IF+I1+13DMB+[100MHZ+1500MHZ]+ARMONICOS+CON+IN100MHZ.CSV"
path2           ="image_and_csv/csv/RF_IF/TRACE1:AISLACION+RF+IF+I1+13DMB+[100MHZ+1500MHZ]+ARMONICOS+CON+IN300MHZ.CSV"
path3           ="image_and_csv/csv/RF_IF/TRACE1:AISLACION+RF+IF+I1+13DMB+[100MHZ+1500MHZ]+ARMONICOS+CON+IN400MHZ.CSV"
path4           ="image_and_csv/csv/RF_IF/TRACE1:AISLACION+RF+IF+I1+13DMB+[100MHZ+1500MHZ]+ARMONICOS+CON+IN500MHZ.CSV"
path5           ="image_and_csv/csv/RF_IF/TRACE1:AISLACION+RF+IF+I1+13DMB+[100MHZ+1500MHZ]+ARMONICOS+CON+IN1000MHZ.CSV"



############ Aislacion RF-IF-Io1
# value           = ['0 dBm','10 dBm','15 dBm']
# outputPort      = 'Io1'
# numerosCsv      = 3
# path1           ="image_and_csv/csv/RF_IF/TRACE1:AISLACION+RF+IF+I1+0DMB+[500MHZ+1500MHZ].CSV"
# path2           ="image_and_csv/csv/RF_IF/TRACE2:AISLACION+RF+IF+I1+10DMB+[500MHZ+1500MHZ].CSV"
# path3           ="image_and_csv/csv/RF_IF/TRACE3:AISLACION+RF+IF+I1+13DMB+[500MHZ+1500MHZ].CSV"

#######################################
############Aislacion RF-IF-Io2
# value           = ['0 dBm','10 dBm','15 dBm']
# outputPort      = 'Io2'
# numerosCsv      = 2
# path1           ="image_and_csv/csv/TRACE1:RFQ+IF+I2+10DBM[0MHZ+2000MHZ].CSV"
# path2           ="image_and_csv/csv/TRACE1:RFQ+IF+I2+15DBM[0MHZ+2000MHZ].CSV"

#######################################
## Aislacion RF-IF-Qo1
# 

#######################################
## Aislacion RF-IF-Qo2
# value           = ['10 dBm','15 dBm']
# outputPort      = 'Qo2'
# numerosCsv      = 2
# path1           ="image_and_csv/csv/TRACE1:RFQ+IF+Q2+10DBM[0MHZ+2000MHZ].CSV"
# path2           ="image_and_csv/csv/TRACE1:RFQ+IF+Q2+10DBM[0MHZ+2000MHZ].CSV"

def aislacionLo_Io(data,inputdBm):
    inputdBmMixer   = int(inputdBm.rsplit(' ')[0]) - 8.5 - 4.0
    return    np.abs(np.array(data) - inputdBmMixer)

def aislascionRf_If(data,inputdBm):
    inputdBmMixer   = int(inputdBm.rsplit(' ')[0]) - 8.5 #tengo solo encuenta el spliter que divide la potencia
    result          = np.abs(np.array(data) - inputdBmMixer)
    return np.array(result)

def atenuacion_Spliter(data,inputdBm):
    dBm       = int(inputdBm.rsplit(' ')[0])- np.array(data) 
    atte      = np.mean(np.extract(np.array(dBm)<0,dBm))
    return atte

# paths         = [path1]
# paths       = [path1,path2]
# paths       = [path1,path2,path3]
paths       = [path1,path2,path3,path4,path5]
placa       = 'Placa1'
tilte       ='{}_{}_{}'.format(tema,outputPort,placa)

plt.figure(tema)
for i in range(numerosCsv):
    csv_data        = extratCSV(paths[i])
    frequency       = csv_data.get_frequency()
    ##############
    # #Aislacion IO-IF
    # dBm             =aislacionLo_Io(csv_data.get_dBm(),value[i])
    ##############
    ##Aislacion RF-IF
    # dBm             =aislascionRf_If(csv_data.get_dBm(),value[0])
    dBm = csv_data.get_dBm()
    ##Spliter en cuadratura 
    # atte      = atenuacion_Spliter(csv_data.get_dBm(),value[i])
    ##############
    plt.plot(frequency,dBm,label=value[0]+" "+inFrequency[i])#'\n Atenuacion Promedio: ' + str(round(atte,3)))
    # print(np.mean(np.extract(np.abs(dBm))))
    plt.legend(title='Input({}) power [dBm]'.format('LO'))


plt.title(tilte);plt.xlabel('Frequency[Hz]');plt.ylabel('Isolation[dB]')
plt.grid(True)
# plt.ylim(-50,0)
plt.xlim(50*10**6,1.5*10**9)
# plt.savefig('/home/dario/Documentos/funda/fiMediciones/DSA815/image_and_csv/image/{}.jpg'.format(tilte))
plt.show()