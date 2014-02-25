#!/usr/bin/python
""" Functions in here handle loading bitlash programs onto the Arduino. """
# import _error # might need this if we actually caught exceptions?
try: import serial
except Exception: print "NO SERIAL MODULE DETECTED"
try: import fdpexpect
except Exception: print "NO FDPEXPECT MODULE DETECTED"
import time

def waitprompt(c):
    """ Wait until we see a prompt. """
    c.expect('\n> ')
    time.sleep(0.1)

def makeprg(setup, loop):
    """ We can only handle one line prgs with no setup right now... """
    return loop

def load(device, baud, program):
    serialport = serial.Serial(device, baud, timeout=0)
    c = fdpexpect.fdspawn(serialport.fd)
    c.sendline('')
    waitprompt(c)
    for line in program:
        line = line.strip()
        if (len(line) > 0) and (line[0] != '#'):
            c.sendline(line)
            waitprompt(c)
    c.close()

if __name__ == "__main__":
    prog = ["function myf {while 1 {twinkle();}}",
            "function startup {run myf}",
            "boot"]
    load('/dev/ttyACM0', 57600, prog)

