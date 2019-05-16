#!/usr/bin/python3

import json

class Current():
     
    def __init__(self, Home="none", Enter="none", Desk="none"):
        self.name = "Current Object"
        self.Home = Home
        self.Enter = Enter
        self.Desk = Desk

    def __str__(self):
        return ("[{}]: \n\t{}".format(self.name, self.__dict__))

    def SetHome(self, Home):
        if (Home):
            self.Home = "#" + Home
        else:
            self.Home = "#f4f4f4"

    def SetEnter(self, Enter):
        if (Enter):
            self.Enter = "#" + Enter
        else:
            self.Enter = "#f4f4f4"
    
    def SetDesk(self, Desk):
        if (Desk):
            self.Desk = "#" + Desk
        else:
            self.Desk = "#f4f4f4"
