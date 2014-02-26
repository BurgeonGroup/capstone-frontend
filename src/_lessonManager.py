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
        self.lesson = None
        self.lessons = ConfigParser.ConfigParser()
        self.lessons.read('content/lessons.ini')

        self.saveFilePath = None
        self.modified = False

        self.header = ReadFile('content/header.html')
        self.footer = ReadFile('content/footer.html')

    def Change(self, lesson):
        sections = self.lessons.sections()
        if(lesson in sections):
            self.lesson = lesson
            return True
        elif isinstance( lesson, int ):
            if(lesson >= 0 and lesson < len(sections)):
                self.lesson = sections[lesson]
                return True
        return False

    def Previous(self):
        if(self.lesson == None):
            return self.First()
        return self.Change(self.lessons.sections().index(self.lesson) - 1)

    def Next(self):
        if(self.lesson == None):
            return self.First()
        return self.Change(self.lessons.sections().index(self.lesson) + 1)

    def First(self):
        return self.Change(0)

    def GetInstructions(self):
        return str(self.header) + ReadFile('lessons/' + self.lesson + '.html') + str(self.footer)

    def GetName(self):
        return self.lesson + ") " + self.lessons.get(self.lesson, "name")

    def HasMain(self):
        return self.lessons.has_option(self.lesson, "main")

    def HasLoop(self):
        return self.lessons.has_option(self.lesson, "loop")

    def StoreCode(self, main, loop):
        self.code[self.lesson] = [main, loop]

    def LoadCode(self):
        if(self.lesson in self.code.keys()):
            return self.code[self.lesson]

        code = ["",""]
        if(self.lessons.has_option(self.lesson, "main")):
            code[0] = self.lessons.get(self.lesson, "main").replace('\\n',"\n").replace('\\t',"\t")
        if(self.lessons.has_option(self.lesson, "loop")):
            code[1] = self.lessons.get(self.lesson, "loop").replace('\\n',"\n").replace('\\t',"\t")
        return code

# Read data from a file
def ReadFile(filepath):
    try:
	      with open(filepath) as f:
	          content = f.readlines()
	          return '\r\n'.join(content)
    except:
	return "File Not Found: " + filepath

if __name__ == '__main__':
    pass # test _lesson.py
