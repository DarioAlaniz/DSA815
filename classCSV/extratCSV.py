import numpy as np
class extratCSV:
    def __init__(self,path):
        self.path = path

    def get_data(self):
        return np.genfromtxt(self.path,skip_header=2,usecols=(0,2),dtype=np.float32,delimiter=",")

    def get_param(self,data):
        frequency = []
        dBm = []
        for row in data:
            frequency.append(row[0])
            dBm.append(row[1])
        return [frequency,dBm]
    
    def get_frequency(self):
        return self.get_param(self.get_data())[0]
    
    def get_dBm(self):
        return self.get_param(self.get_data())[1]
    