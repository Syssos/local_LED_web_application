#!/usr/bin/python3

import serial
import uuid
import json

class Lighty():
     
    def __init__(self, name="NA", Color="NA", ledcount="NA", stripcount="NA", Pattern="NA"):
        self.name = name
        self.ID = str(uuid.uuid4())
        self.SerialPort = "Configure"
        self.CurrentColor = Color
        self.Pattern = Pattern
        self.LEDinfo = {"LED Count": ledcount, "StripCount": stripcount}

    def __str__(self):
        return ("[{}]: \n\t{}".format(self.name, self.__dict__))

    # def SerialConnected(self)
    #     """ Returns True if objects serial port is connected.
    #     """
    #     if ():
    #         return True
    #     return False

    # def SendColor(self, Color):
    #     if (Connectard()):
    #         self.SerialPort.open()
    #         self.SerialPort.write("#000001\n")
    #         self.SerialPort.close()
    #     else:


    # def Connectard(self):
    #     try:
    #         self.SerialPort = serial.Serial()
    #         self.SerialPort.baudrate = 19200
    #         self.SerialPort.port = "COM1"
    #         return True
    #     except Exception as e:
    #         print("Error: [{}]".format(e))
    #         return False