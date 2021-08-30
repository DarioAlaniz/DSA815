#from _typeshed import Self
import vxi11
import unittest

class DSA815(vxi11.Instrument):
    def __init__(self, host, *args, **kwargs):
        super(DSA815, self).__init__(host, *args, **kwargs)
    def get_identification(self):
        return self.ask("*IDN?")
    def set_center_frequency(self,frequency):
        self.write("SENSe:FREQuency:CENTer {}".format(frequency))
    def get_center_frequency(self):
        return self.ask("SENSe:FREQuency:CENTer?")
    def set_span(self,frequency):
        self.write("SENSe:FREQuency:SPAN 20000000")
    def get_span(self):
        return self.ask("SENSe:FREQuency:SPAN?")
    def set_span_full(self):

        self.write("SENSe:FREQuency:SPAN:FULL ")

    def get_trace(self,n=1,name='T1',path='D'):
        self.write("MMEMory:STORe:TRACe TRACE{},{}:{}.csv".format(n,path,name))

    def get_trace_info(self):
        return self.ask("MMEMory:DISK:INFormation?")
    def set_screen(self,name='screen'):
        self.write("MMEMory:STORe:SCReen E:\{}.jpg".format(name))

    def get_ptable(self,name='pt1',path='D'):
        self.write("MMEMory:STORe:PTAB {}:\{}.csv".format(path,name))
    

########################################################################


# def main():
#     instrument = DSA815('172.16.0.110')
#     print(instrument.get_identification())
#     instrument.get_trace(path='E:\Trace1',name='LO+IF+10dBm[500Mhz+1500Mhz]')



# if __name__ == "__main__":
#     main()
# nombre = 'LO+IF+Q2+13DBM[675MHZ+1500MHZ]'
instrument = DSA815('172.16.0.110')
print("Conectado a : "+instrument.get_identification())
print("Obteniendo Resultados.....")
if(1):#Trace
    nombre      = 'aislacion+Rf+If+Q1+10DMB+[500Mhz+1500Mhz]'
    numTrace    = 1
    instrument.get_trace(path='E:\Trace{}'.format(numTrace),name=nombre,n=numTrace)
if(0):#peak table
    nombre = 'peaktable[input5dBm]'
    instrument.get_trace(path='E',name=nombre)
if(0):
    nombre='Aislacion+RF+IF+Io1[100Mhz+13dBM]'
    instrument.set_screen(name=nombre)
