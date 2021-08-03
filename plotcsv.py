import matplotlib.pyplot as plt
import numpy as np
path1 = "../image_and_csv/TRACE1:LO+IF+10DBM[500MHZ+1500MHZ].CSV"
path2 = "../image_and_csv/TRACE1:LO+IF+15DBM[500MHZ+1500MHZ].CSV"
path3 = "../image_and_csv/TRACE1:LO+IF+20DBM[500MHZ+1500MHZ].CSV"

dataIo_IF_10dBm = np.genfromtxt(path1,skip_header=2,usecols=(0,2),dtype=np.float32,delimiter=",")
dataIo_IF_15dBm = np.genfromtxt(path2,skip_header=2,usecols=(0,2),dtype=np.float32,delimiter=",")
dataIo_IF_20dBm = np.genfromtxt(path3,skip_header=2,usecols=(0,2),dtype=np.float32,delimiter=",")

print(len(dataIo_IF_15dBm))
frequency1 = []
dBm1 =[]
frequency2 = []
dBm2 =[]
frequency3 = []
dBm3 =[]
for row in dataIo_IF_10dBm:
    frequency1.append(row[0])
    dBm1.append(row[1])
for row in dataIo_IF_15dBm:
    frequency2.append(row[0])
    dBm2.append(row[1])
for row in dataIo_IF_20dBm:
    frequency3.append(row[0])
    dBm3.append(row[1])


plt.figure(1)
plt.plot(frequency1,dBm1);plt.plot(frequency2,dBm2);plt.plot(frequency3,dBm3)
plt.legend('10dBm')
plt.show()

