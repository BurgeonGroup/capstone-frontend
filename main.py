#!/usr/bin/python
""" This is the main program file. """
from src import _interface
from src import _loader
from src import _finddev
from src import _error
import wx

class MyApp(wx.App):
    """ Main application. """

    def load(self, setup, loop):
        """ Use _loader module to load program onto Arduino via serial. """
        self.loader.load(setup, loop)
        self.frame.StatusBar.SetStatusText("Done")
        return error

    def OnInit(self):
        """ Initialize application config and then interface config. """
        # we don't like to overide __init__ for wx.App so vars defined here
        self.loader = _loader.Loader(_finddev.finddev(), 57600)
        self.frame = _interface._interface(self)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True # return success flag


if __name__ == '__main__':
    app = MyApp(None)
    app.MainLoop()

