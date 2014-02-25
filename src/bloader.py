#! /usr/bin/python
import serial, fdpexpect, sys, time, commands

def waitprompt(c):
	c.expect('\n> ')
	time.sleep(0.1)

def load(device, baud, program):
    serialport = serial.Serial(device, baud, timeout=0)
    c = fdpexpect.fdspawn(serialport.fd)
    #c.logfile_read = sys.stdout
    # synch with the command prompt
    c.sendline('')
    waitprompt(c)
    # do stuff
    for line in program:
        line = line.strip()
        if (len(line) > 0) and (line[0] != '#'):
            c.sendline(line)
            waitprompt(c)
    c.close()

if __name__ == "__main__":
    program = ["pixel(0, 0, green); draw_all()\n"]
    load('/dev/ttyACM0', 57600, program)

