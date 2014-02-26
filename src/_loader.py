#!/usr/bin/python
""" Functions in here handle loading bitlash programs onto the Arduino. """
# import _error # might need this if we actually caught exceptions?
import serial, fdpexpect, time
from multiprocessing import Process

def waitprompt(c):
    """ Wait until we see a prompt. """
    c.expect('\n> ')
    time.sleep(0.1)

def load(device, baud, program):
    serialport = serial.Serial(device, baud, timeout=0)
    c = fdpexpect.fdspawn(serialport.fd)
    c.sendline('')
    waitprompt(c)
    for line in program.splitlines():
        line = line.strip()
        if (len(line) > 0) and (line[0] != '#'):
            c.sendline(line)
            waitprompt(c)
    c.close()


class Loader:
    def __init__(self, device, baud):
        self.device = device
        self.baud = baud
        self.proc = None

    def load(self, program):
        if self.proc is not None:
            self.proc.terminate()
        self.proc = Process(target=load,
                            args=(self.device, self.baud, program))
        self.proc.start()


if __name__ == "__main__":
    l = Loader('/dev/ttyACM0', 57600)
    while True: l.load(raw_input("> "))

