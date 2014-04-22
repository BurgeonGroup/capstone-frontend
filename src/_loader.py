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

# replace \t and \n with a space and multiple spaces with a single space
def make_single_line(prg):
    prg = prg.strip()
    prg = re.sub("\n", " ", prg) # replace new lines with semicolons
    prg = re.sub("\t", " ", prg) # replace tabs with spaces
    prg = re.sub("[ ]+", " ", prg) # replace multiple spaces with a single space
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
        ser = serial.Serial(self.device, self.baud)
        time.sleep(1.5) # let Arduino bootloader timeout
        setup = make_single_line(setup)
        loop = make_single_line(loop)
        ser.write(setup)
        print "setup: " + setup # test
        print "loop: " + loop # test

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 57600)
    time.sleep(1.5)
    ser.write("twinkle(red)")

