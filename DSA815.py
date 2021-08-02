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
        print("Center Frequency: ", self.ask("SENSe:FREQuency:CENTer?"))
    def set_span(self,frequency):
        self.write("SENSe:FREQuency:SPAN 20000000")
    def get_span(self):
        print("Span Frequency: ", self.ask("SENSe:FREQuency:SPAN?"))


########################################################################


def main():
    instrument = DSA815('172.16.0.110')
    print(instrument.get_identification())
    instrument.get_span()

if __name__ == "__main__":
    main()