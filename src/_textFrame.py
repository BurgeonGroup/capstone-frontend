# -*- coding: utf-8 -*-
#
# touch-editor is based on wx.stc.StyledTextCtrl
# author : juntao.qiu@gmail.com
# date   : 2012/02/11
#
import wx
import wx.stc as stc

import re
import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')

import HelperUtil

class CodeTextCtrl(stc.StyledTextCtrl):

    faces = {
        'times': 'Courier New',
        'mono' : 'Courier New',
        'helv' : 'Courier New',
        'other': 'Courier New',
        'size' : 16,
        'linesize': 10,
    }

    def getBMarkerNumber(self):
        return self.BMarkerNumber

    def __init__(self, parent, ID, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        stc.StyledTextCtrl.__init__(self, parent, ID, pos, size, style)

        self.helper = HelperUtil.CommonHelper([])

        self.isBundleMode = False
        self.currentSnippet = None
        self.hasOutdentWord = re.compile(r"\b(?:break|continue|return)\b")
        self.lineEnding = '\n'
        self.BMarkerNumber = 10

        self.macro = []

        # ctrl-+(in), ctrl--(out)
        self.CmdKeyAssign(ord('+'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.CmdKeyAssign(ord('-'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)

        self.Bind(stc.EVT_STC_UPDATEUI, self.OnUpdateUI)
        self.Bind(stc.EVT_STC_CHARADDED, self.OnCharAdded)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)

        self.StyleClearAll()  # Reset all to be like the default
        self.InitUI()

    def InitMargin(self):
        #using margin 1 to be line-number
        self.SetMarginWidth(0, 32)
        self.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
        #clear number-panel's mask
        self.SetMarginMask(0, 0)

    def InitStyle(self):#{{{
        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % self.faces)
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER,  "back:#C0C0C0,face:%(helv)s,size:%(linesize)d" % self.faces)
        self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % self.faces)
        self.StyleSetSpec(stc.STC_STYLE_BRACELIGHT,  "fore:#FFFFFF,back:#0000FF,bold")
        self.StyleSetSpec(stc.STC_STYLE_BRACEBAD,    "fore:#000000,back:#FF0000,bold")
        self.StyleClearAll()  # Reset all to be like the default

        # Default
        self.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % self.faces)
        # Comments
        self.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % self.faces)
        # Number
        self.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % self.faces)
        # String
        self.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % self.faces)
        # Single quoted string
        self.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % self.faces)
        # Keyword
        self.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % self.faces)
        # Triple quotes
        self.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % self.faces)
        # Triple double quotes
        self.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % self.faces)
        # Class name definition
        self.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % self.faces)
        # Function or method name definition
        self.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % self.faces)
        # Operators
        self.StyleSetSpec(stc.STC_P_OPERATOR, "bold,size:%(size)d" % self.faces)
        # Identifiers
        self.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % self.faces)
        # Comment-blocks
        self.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % self.faces)
        # End of line where string is not closed
        self.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % self.faces)#}}}

    def InitUI(self):#{{{
        keywords = self.helper.GetKeywords()
        self.SetLexer(stc.STC_LEX_CPP)
        #self.SetKeyWords(0, " ".join(ckeys)+" ".join(plkeys))
        self.SetKeyWords(0, " ".join(keywords))
        #self.SetKeyWords(1, " ".join(plkeys))
        self.SetProperty("fold", "1")
        #keywords and other words has same size
        self.SetProperty("tab.timmy.whinge.level", "1")

        self.SetIndent(4)
        self.SetTabIndents(True)
        self.SetTabWidth(4)
        self.SetUseTabs(False)
        self.SetIndentationGuides(True)
        self.SetViewWhiteSpace(False)

        self.SetEdgeMode(stc.STC_EDGE_LINE)
        self.SetEdgeColumn(80)
        self.SetScrollWidth(100)

        self.InitMargin()
        self.InitStyle()

        self.SetSelBackground(True, "#316AC5")
        self.SetSelForeground(True, wx.WHITE)
        self.SetCaretForeground("BLUE")

        #highlight the current line
        self.SetCaretLineVisible(True)
        #wxPythonInAction : #FFFFCC, UE: #C4E8FD
        self.SetCaretLineBackground("#C4E8FD")

        #self.SetWrapStartIndent(1)
        # register some images for use in the AutoComplete box.
        #self.RegisterImage(1, wx.Image("extra/icons/method.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        #self.RegisterImage(2, wx.Image("extra/icons/keyword.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        #self.RegisterImage(3, wx.Image("extra/icons/function.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap())

        self.InitAutoComp()#}}}

    def InitAutoComp(self):
        self.AutoCompSetIgnoreCase(True)
        self.AutoCompSetAutoHide(False)
        self.AutoCompSetChooseSingle(False)
        self.AutoCompSetDropRestOfWord(False)
        self.AutoCompStops("([{,")

    def SetTitle(self, title):
        self.title = title

    def GetTitle(self):
        return self.title

    def TryShowCallTip(self, currentPos, word):
        #print word, fdmap[word]
        fdmap = self.helper.GetFunctionMap()
        if word in fdmap.keys():
            self.CallTipShow(currentPos, fdmap[word])
        else:
            return

    def OnCharAdded(self, event):#{{{
        if self.CallTipActive():
            self.CallTipCancel()

        charc = event.GetKey()

        #if self.isBundleMode:
        #    snippet = self.currentSnippet
        #    snippet.Update(charc)

        if self.AutoCompActive():
            return
        # check if current style is a string or a comment
        currentPos = self.GetCurrentPos()
        try:
            entire_text = self.GetTextRange( self.PositionFromLine( self.GetCurrentLine() ), currentPos - 1 ) # wx2.5.2.9
            entire_text_all = self.GetTextRange( self.PositionFromLine( self.GetCurrentLine() ), currentPos)
        except:
            evt.Skip()
            return

        word = entire_text.strip().split('.')[-1:][0].split(' ')[-1:][0].strip()
        #print word

        #code calltips
        if chr(charc) == "(" and self.CallTipActive() == 0:
            if self.BraceMatch(currentPos-1) == -1:
                if self.GetCharAt(currentPos) != 40:
                    #sself.AddText(')')
                    self.SetSelection(currentPos, currentPos)
                self.TryShowCallTip(currentPos, word)
            return False

        # Auto END string
        elif chr(charc) == '"' and \
                         self.GetLineEndPosition(self.LineFromPosition(currentPos)) == currentPos:
            #self.AddText('"')
            self.SetSelection(currentPos, currentPos)
            return False
        elif chr(charc) == '\'' and \
                         self.GetLineEndPosition(self.LineFromPosition(currentPos)) == currentPos:
            #self.AddText('\'')
            self.SetSelection(currentPos, currentPos)
            return False
        elif chr(charc) == '[' and \
                         self.GetLineEndPosition(self.LineFromPosition(currentPos)) == currentPos:
            #self.AddText(']')
            self.SetSelection(currentPos, currentPos)
            return False
        elif chr(charc) == '{' and \
                         self.GetLineEndPosition(self.LineFromPosition(currentPos)) == currentPos:
            #self.AddText('}')
            self.SetSelection(currentPos, currentPos)
            return False#}}}

    def DupCurrentLine(self):
        lno = self.GetCurrentLine()
        if len(self.GetLine(lno)) == 0:
            pass
        self.LineDuplicate()
        self.GotoLine(lno+1)
        self.LineEnd()

    def DelCurrentLine(self):
        lno = self.GetCurrentLine()
        self.LineDelete()
        self.GotoLine(lno-1)
        self.LineEnd()

    def AutoIndent(self):#{{{
        lno = self.GetCurrentLine()
        pos = self.GetCurrentPos()
        col = self.GetColumn(pos)

        lstart = self.PositionFromLine(lno)
        line = self.GetLine(lno)[:pos-lstart]
        index = self.GetLineIndentation(lno)
        n = 0
        if col <= index:
            n = col
        elif pos:
            n = index

        if len(line) == 0:
            pass
        elif line[-1:] == "\\":
            if lno > 1:
                prl = self.GetLine(lno-1)
                if prl[-2:] == "\\\n":
                    n -= self.GetIndent()
            n += self.GetIndent()
        elif line[-1:] in "([":
            n += self.GetIndent()
        elif n >= self.GetIndent():
            if self.hasOutdentWord.search(line, index) is not None:
                n -= self.GetIndent()
            elif lno > 1:
                prl = self.GetLine(lno-1)
                #print prl
                if prl[-2:] == "\\\n" and n >= self.GetIndent():
                    n -= self.GetIndent()
        text = n*' '
        if self.GetUseTabs():
            text = text.replace(self.GetTabWidth()*' ', '\t')

        self.ReplaceSelection(self.lineEnding + text)#}}}

    def GetWordAtPos(self, pos):
        word = ''
        x = pos
        while x != wx.stc.STC_INVALID_POSITION:
            ch = self.GetCharAt(x)
            if ch <= 32 or ch > 128:
                if x != pos:
                    break
            word = chr(ch) + word
            x = x - 1
        return word.strip()

    def OnKeyPressed(self, event):#{{{
        if self.CallTipActive():
            self.CallTipCancel()

        key = event.GetKeyCode()

        #duplicate a line and move next end
        if key == ord('D') and event.ControlDown():
            self.DupCurrentLine()
        #delete a line and move privous start
        elif key == ord('U') and event.ControlDown():
            self.DelCurrentLine()
        #move cursor down
        elif key == ord('N') and event.ControlDown():
            self.GotoLine(self.GetCurrentLine()+1)
        #move cursor up
        elif key == ord('P') and event.ControlDown():
            self.GotoLine(self.GetCurrentLine()-1)
        #handle bundles here
        elif key == wx.WXK_TAB:
            #print self.isBundleMode
            pos = self.GetCurrentPos()
            word = self.GetWordAtPos(pos)
            line = self.GetCurrentLine()

            #The very first time of BundleMode, init the snippetPos, gotoline, etc
            #if not self.isBundleMode: #word in self.snippets.keys() and
            #    self.isBundleMode = True
                #instance = TouchSnippet.TouchSnippet(self.snippets[word])
                #instance.Build()
                #snippet = instance.Arrange()
                #self.currentSnippet = instance
           #     self.DelWordLeft()
                #self.AddText(snippet)
           #     self.GotoLine(line)
                #self.snippetLine = line
                #self.snippetPos = pos - len(word)

            #move to next position
            #if self.isBundleMode:
                #if event.ShiftDown():
                #    start, end = self.currentSnippet.PrevPos()
                #else:
                #    start, end = self.currentSnippet.NextPos()

                #if (start, end) == (-1, -1):
                    #self.isBundleMode = False
                    #self.snippetPos = -1
                    #self.currentSnippet = None
                    #return

                #self.SetSelection(self.snippetPos+start, self.snippetPos+end)
                #pass
            #else:
            event.Skip()

            keywords = self.helper.GetKeywords()
            udkeys = self.helper.GetUserKeywords()

            #auto-complete
            if event.ControlDown():
                conds = []
                for i in range(len(keywords)):
                    if keywords[i].startswith(word.lower()):
                        conds.append(keywords[i] + '?2')
                for i in range(len(udkeys)):
                    if udkeys[i].startswith(word.lower()):
                        conds.append(udkeys[i] + '?3')
                if len(conds) > 0:
                    conds.sort()
                    end = self.GetCurrentPos()
                    start = end - len(word)
                    self.AutoCompShow(len(word), " ".join(conds))

        elif key == 13 or key == 14:
            if self.AutoCompActive():
                return self.AutoCompComplete()
            self.AutoIndent()
        elif key == ord('T') and event.ControlDown():
            pos = self.GetCurrentPos()
        else:
            event.Skip()#}}}


    def OnUpdateUI(self, event):#{{{
        if self.AutoCompActive() or self.CallTipActive():
            return
        #update the status bar
        row = self.GetCurrentLine()
        pos = self.GetCurrentPos()
        col = self.GetColumn(pos)
        msg = {}
        msg['type'] = "pos"
        msg['row'] = row+1
        msg['col'] = col

        # check for matching braces
        braceAtCaret = -1
        braceOpposite = -1
        charBefore = None
        caretPos = self.GetCurrentPos()

        if caretPos > 0:
            charBefore = self.GetCharAt(caretPos - 1)
            styleBefore = self.GetStyleAt(caretPos - 1)

        # check before
        if charBefore and chr(charBefore) in "[]{}()" and styleBefore == stc.STC_P_OPERATOR:
            braceAtCaret = caretPos - 1

        # check after
        if braceAtCaret < 0:
            charAfter = self.GetCharAt(caretPos)
            styleAfter = self.GetStyleAt(caretPos)

            if charAfter and chr(charAfter) in "[]{}()" and styleAfter == stc.STC_P_OPERATOR:
                braceAtCaret = caretPos

        if braceAtCaret >= 0:
            braceOpposite = self.BraceMatch(braceAtCaret)

        if braceAtCaret != -1  and braceOpposite == -1:
            self.BraceBadLight(braceAtCaret)
        else:
            self.BraceHighlight(braceAtCaret, braceOpposite)#}}}
