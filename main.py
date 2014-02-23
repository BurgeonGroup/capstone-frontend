#!/usr/bin/python
""" This is the main program file. """
from src import _lesson
from src import _interface
from src import _loader
from src import _finddev
from src import _error
import wx

class MyApp(wx.App):
    """ Main application. """

    def load(self, loop):
        """ Use _loader module to load program onto Arduino via serial. """
        if not(_finddev.exists(self.dev)):
            self.dev = _finddev.finddev()
        if self.dev == "":
            self.frame.StatusBar.SetStatusText("ERROR: Unable to communicate with the Arduino LED Matrix")
            return _error.Error(_error.ARDUINO_NOT_FOUND)
        prg = _loader.makeprg("", loop)

        # _loader.load might return something other than None in future
        error = _loader.load(self.dev, self.baud, prg)
        self.frame.StatusBar.SetStatusText("Done")
        return error

    def OnInit(self):
        """ Initialize application config and then interface config. """
        # we don't like to overide __init__ for wx.App so vars defined here

        self.dev = _finddev.finddev()
        self.baud = 57600

        self.lessonsManager = _lesson.LessonManager()

        self.frame = _interface._interface(self, self.lessonsManager)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        self.frame.StatusBar.SetStatusText("Ready")

        return True # return success flag


if __name__ == '__main__':
    app = MyApp(None)
    app.MainLoop()

