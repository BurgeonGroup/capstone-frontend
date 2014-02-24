#!/usr/bin/python
""" Define Lesson class that holds lesson data to be used by the interface.
Lesson text is loaded from html files in lessons/. Main program will just
call get_lessons to get a list of all lessons that the interface should
present. """

import os
import ConfigParser

class LessonManager:
    """ Basically just a struct of lesson related data. """

    def __init__(self):

        self.code = {}
        self.number = 1
        self.lessons = ConfigParser.ConfigParser()
        self.lessons.read('content/lessons.ini')

        self.saveFilePath = None
        self.modified = False

        self.header = ReadFile('content/header.html')
        self.footer = ReadFile('content/footer.html')

    def ChangeLesson(self, number):
        if(self.Exists(number)):
            self.number = number

    def PreviousLesson(self):
        self.ChangeLesson(self.number - 1)

    def NextLesson(self):
        self.ChangeLesson(self.number + 1)

    def GetInstructions(self):
        return str(self.header) + ReadFile('lessons/lesson'+str(self.number)+'.html') + str(self.footer)

    def GetName(self):
        return str(self.number) + ") " + self.lessons.get("Lesson"+str(self.number), "name")

    def ShowMain(self):
        return self.lessons.getboolean("Lesson"+str(self.number), "main")

    def ShowLoop(self):
        return self.lessons.getboolean("Lesson"+str(self.number), "loop")

    def StoreCode(self, code):
        self.code[self.number] = code

    def LoadCode(self):
        if(self.number in self.code.keys()):
            return self.code[self.number];
        else:
            return "main(){\n\n\t//Insert Code Here\n\n}"

    def Exists(self, number):
        return self.lessons.has_section("Lesson"+str(number))


# Read data from a file
def ReadFile(filepath):
    try:
	      with open(filepath) as f:
	          content = f.readlines()
	          return '\r\n'.join(content)
    except:
	return False

if __name__ == '__main__':
    pass # test _lesson.py
