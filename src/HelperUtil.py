# -*- coding: utf-8 -*-
#
# touch-editor is based on wx.stc.StyledTextCtrl
# author : juntao.qiu@gmail.com
# date   : 2012/02/11
#

class CommonHelper(object):
    # function declareation map
    fdmap = {}
    # user-define keywords
    udkeys = []
    #pre-defined keywords
    keywords = ['if']

    def __init__(self, ext):
        self.ext = ext
        self.loadKeywords()
        self.loadTips()

    def loadFileToList(self, file, list):
        f = open(file, "rb")
        if not f:
            return
        line = f.readline()
        while line:
            list.append(line.strip())
            line = f.readline()

        f.close()

    def loadKeywords(self):
        self.loadFileToList("content/python.kw", self.keywords)
        #self.loadFileToList("extra\oracle.kw", self.keywords)
        self.keywords.sort()

    def loadTips(self):
        return
        f = open("extra\idp.api", "rb")
        if not f:
            return

        line = f.readline()
        while line:
            pos = line.find('(')

            if pos == -1:
                self.udkeys.append(line)
                line = f.readline()
                continue
            else:
                key = line[:pos]
                value = line
                self.fdmap[key] = line
                self.udkeys.append(key)
            line = f.readline()

        f.close()
        return

    def GetKeywords(self):
        return self.keywords

    def GetFunctionMap(self):
        return self.fdmap

    def GetUserKeywords(self):
        return self.udkeys

if __name__ == "__main__":
    helper = CommonHelper([])
    print helper.GetKeywords()
    print helper.GetFunctionMap()
    print helper.GetUserKeywords()
