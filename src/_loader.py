#!/usr/bin/python
""" Functions in here handle loading bitlash programs onto the Arduino. """
# import _error # might need this if we actually caught exceptions?
import serial, fdpexpect, time
from multiprocessing import Process
import re

def waitprompt(c):
    """ Wait until we see a prompt. """
    c.expect('\n> ')
    time.sleep(0.1)

def make_single_line(prg):
    prg = re.sub("\n", " ", prg)
    prg = re.sub("\t", " ", prg)
    prg = re.sub("[ ]+", " ", prg)
    return prg

def load(device, baud, setup, loop):
    serialport = serial.Serial(device, baud, timeout=0)
    c = fdpexpect.fdspawn(serialport.fd)
    c.sendline('')
    waitprompt(c)
    for line in setup.splitlines():
        line = line.strip()
        if (len(line) > 0) and (line[0] != '#'):
            c.sendline(line)
            waitprompt(c)
    while True:
        for line in loop.splitlines():
            line = line.strip()
            if (len(line) > 0) and (line[0] != '#'):
                c.sendline(line)
                waitprompt(c)
    c.close() # unreachable ...


class Loader:
    def __init__(self, device, baud):
        self.device = device
        self.baud = baud
        self.proc = None

    def load(self, setup, loop):
        setup = make_single_line(setup)
        loop = make_single_line(loop)
        print "setup: " + setup # test
        print "loop: " + loop # test
        # TODO: check to see if the device is still there...
        if self.proc is not None:
            self.proc.terminate()
        self.proc = Process(target=load,
                            args=(self.device, self.baud, setup, loop))
        self.proc.start()


if __name__ == "__main__":
    l = Loader('/dev/ttyACM0', 57600)
    while True: l.load(raw_input("setup: "), raw_input("loop: "))

