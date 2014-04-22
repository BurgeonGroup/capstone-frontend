# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html2
import _textFrame

###########################################################################
## Class _mainFrame
###########################################################################

class _mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Blink", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL, name = u"MainWindow" )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.LessonName = wx.StaticText( self, wx.ID_ANY, u"IF Statements", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LessonName.Wrap( -1 )
		self.LessonName.SetFont( wx.Font( 12, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer8.Add( self.LessonName, 0, wx.ALL, 12 )
		
		
		bSizer6.Add( bSizer8, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PreviousButton = wx.Button( self, wx.ID_ANY, u"Previous", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.PreviousButton, 0, wx.ALL, 1 )
		
		self.NextButton = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.NextButton, 0, wx.ALL, 1 )
		
		
		bSizer6.Add( bSizer7, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer1.Add( bSizer6, 0, wx.ALIGN_RIGHT|wx.EXPAND, 0 )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainContentBox = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.InstructionsWindow = wx.html2.WebView.New(self.m_panel2)
		bSizer9.Add( self.InstructionsWindow, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		self.m_panel2.SetSizer( bSizer9 )
		self.m_panel2.Layout()
		bSizer9.Fit( self.m_panel2 )
		MainContentBox.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel21 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		self.MainPanel = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.MainPanel.SetBackgroundColour( wx.Colour( 247, 247, 247 ) )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Main Function", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 11, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer81.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer81.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Executes only once", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		self.m_staticText22.SetFont( wx.Font( 9, 74, 93, 90, False, "Tahoma" ) )
		self.m_staticText22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer81.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer81, 0, wx.EXPAND, 5 )
		
		self.MainCodeBox = _textFrame.CodeTextCtrl(self.MainPanel, -1)
		self.MainCodeBox.Bind(wx.stc.EVT_STC_CHARADDED, self.OnCodeModified)
		bSizer15.Add( self.MainCodeBox, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.MainPanel.SetSizer( bSizer15 )
		self.MainPanel.Layout()
		bSizer15.Fit( self.MainPanel )
		bSizer91.Add( self.MainPanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.LoopPanel = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.LoopPanel.SetBackgroundColour( wx.Colour( 247, 247, 247 ) )
		
		bSizer772 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer811 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText23 = wx.StaticText( self.LoopPanel, wx.ID_ANY, u"Loop Function", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_staticText23.SetFont( wx.Font( 11, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer811.Add( self.m_staticText23, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer811.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText221 = wx.StaticText( self.LoopPanel, wx.ID_ANY, u"Executes repeatedly ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		self.m_staticText221.SetFont( wx.Font( 9, 74, 93, 90, False, "Tahoma" ) )
		self.m_staticText221.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer811.Add( self.m_staticText221, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer772.Add( bSizer811, 0, wx.EXPAND, 5 )
		
		self.LoopCodeBox = _textFrame.CodeTextCtrl(self.LoopPanel, -1)
		self.LoopCodeBox.Bind(wx.stc.EVT_STC_CHARADDED, self.OnCodeModified)
		bSizer772.Add( self.LoopCodeBox, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.LoopPanel.SetSizer( bSizer772 )
		self.LoopPanel.Layout()
		bSizer772.Fit( self.LoopPanel )
		bSizer91.Add( self.LoopPanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_button3 = wx.Button( self.m_panel21, wx.ID_ANY, u"Play!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetFont( wx.Font( 20, 74, 90, 92, False, "Tahoma" ) )
		self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer91.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 0 )
		
		
		self.m_panel21.SetSizer( bSizer91 )
		self.m_panel21.Layout()
		bSizer91.Fit( self.m_panel21 )
		MainContentBox.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.m_panel1.SetSizer( MainContentBox )
		self.m_panel1.Layout()
		MainContentBox.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem19 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"New"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem19 )
		
		self.SaveButton = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.SaveButton )
		
		self.SaveAsButton = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save As...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.SaveAsButton )
		
		self.OpenButton = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.OpenButton )
		
		self.StartShowButton = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Start Show", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.StartShowButton )
		
		self.ExitButton = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.ExitButton )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.LessonMenu = wx.Menu()
		self.m_menubar1.Append( self.LessonMenu, u"Lesson" ) 
		
		self.m_menu5 = wx.Menu()
		self.m_menuItem10 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem10 )
		
		self.m_menubar1.Append( self.m_menu5, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnApplicationStarted )
		self.Bind( wx.EVT_CLOSE, self.OnApplicationClosing )
		self.PreviousButton.Bind( wx.EVT_BUTTON, self.OnPreviousButtonClicked )
		self.NextButton.Bind( wx.EVT_BUTTON, self.OnNextButtonClicked )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnRunProgramClicked )
		self.Bind( wx.EVT_MENU, self.OnNewClicked, id = self.m_menuItem19.GetId() )
		self.Bind( wx.EVT_MENU, self.OnSaveClicked, id = self.SaveButton.GetId() )
		self.Bind( wx.EVT_MENU, self.OnSaveAsClicked, id = self.SaveAsButton.GetId() )
		self.Bind( wx.EVT_MENU, self.OnOpenClicked, id = self.OpenButton.GetId() )
		self.Bind( wx.EVT_MENU, self.OnStartShowClicked, id = self.StartShowButton.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExitClicked, id = self.ExitButton.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAboutClicked, id = self.m_menuItem10.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnApplicationStarted( self, event ):
		event.Skip()
	
	def OnApplicationClosing( self, event ):
		event.Skip()
	
	def OnPreviousButtonClicked( self, event ):
		event.Skip()
	
	def OnNextButtonClicked( self, event ):
		event.Skip()
	
	def OnRunProgramClicked( self, event ):
		event.Skip()
	
	def OnNewClicked( self, event ):
		event.Skip()
	
	def OnSaveClicked( self, event ):
		event.Skip()
	
	def OnSaveAsClicked( self, event ):
		event.Skip()
	
	def OnOpenClicked( self, event ):
		event.Skip()
	
	def OnStartShowClicked( self, event ):
		event.Skip()
	
	def OnExitClicked( self, event ):
		event.Skip()
	
	def OnAboutClicked( self, event ):
		event.Skip()
	

