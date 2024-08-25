# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame_LoadImage
###########################################################################

class Frame_LoadImage ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Load Image", pos = wx.DefaultPosition, size = wx.Size( 655,326 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel20 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel20, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Select image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_filePicker_Image = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select an image to be loaded", u"Image files (*.bmp;*.png;*.jpeg;*.jpg)|*.bmp;*.png;*.jpeg;*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		fgSizer1.Add( self.m_filePicker_Image, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.Hide()

		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.Hide()

		fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


		sbSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )

		self.m_bitmap_LoadImage = wx.StaticBitmap( self.m_panel20, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 267,200 ), wx.BORDER_SUNKEN )
		bSizer2.Add( self.m_bitmap_LoadImage, 0, wx.ALL, 5 )


		self.m_panel20.SetSizer( bSizer2 )
		self.m_panel20.Layout()
		bSizer2.Fit( self.m_panel20 )
		bSizer42.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel28 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_OK = wx.Button( self.m_panel28, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button_OK, 0, wx.ALL, 5 )

		self.m_button_Cancel = wx.Button( self.m_panel28, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button_Cancel, 0, wx.ALL, 5 )


		self.m_panel28.SetSizer( bSizer10 )
		self.m_panel28.Layout()
		bSizer10.Fit( self.m_panel28 )
		bSizer59.Add( self.m_panel28, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer42.Add( bSizer59, 1, wx.EXPAND, 5 )


		self.m_panel23.SetSizer( bSizer42 )
		self.m_panel23.Layout()
		bSizer42.Fit( self.m_panel23 )
		bSizer46.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer46 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Frame_LoadImageOnClose )
		self.m_filePicker_Image.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_ImageOnFileChanged )
		self.m_button_OK.Bind( wx.EVT_BUTTON, self.m_button_OKOnButtonClick )
		self.m_button_Cancel.Bind( wx.EVT_BUTTON, self.m_button_CancelOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Frame_LoadImageOnClose( self, event ):
		event.Skip()

	def m_filePicker_ImageOnFileChanged( self, event ):
		event.Skip()

	def m_button_OKOnButtonClick( self, event ):
		event.Skip()

	def m_button_CancelOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Frame_WoodKnotLogic
###########################################################################

class Frame_WoodKnotLogic ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Wood Knot Logic", pos = wx.DefaultPosition, size = wx.Size( 873,575 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel26 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel21 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel1 = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Adaptive Threshold" ), wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Mean Filter Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_spinCtrl_MeanFilterSize = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 401 )
		gSizer1.Add( self.m_spinCtrl_MeanFilterSize, 0, wx.ALL, 5 )

		self.m_staticText_Adaptive = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Adaptive Threshold Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Adaptive.Wrap( -1 )

		gSizer1.Add( self.m_staticText_Adaptive, 0, wx.ALL, 5 )

		self.m_spinCtrl_AdaptThreshOffset = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -1000, 1000, 0 )
		gSizer1.Add( self.m_spinCtrl_AdaptThreshOffset, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Light/Dark Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )

		m_choice_LightDarkPartChoices = [ u"Dark Part", u"Light Part" ]
		self.m_choice_LightDarkPart = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_LightDarkPartChoices, 0 )
		self.m_choice_LightDarkPart.SetSelection( 0 )
		gSizer1.Add( self.m_choice_LightDarkPart, 0, wx.ALL, 5 )


		sbSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Erosion" ), wx.VERTICAL )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText11 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Kernel Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_spinCtrl_ErodeKernelSize = wx.SpinCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 20 )
		gSizer4.Add( self.m_spinCtrl_ErodeKernelSize, 0, wx.ALL, 5 )


		sbSizer7.Add( gSizer4, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer7, 1, wx.EXPAND, 5 )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Opening" ), wx.VERTICAL )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText111 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Kernel Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		gSizer5.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_spinCtrl_OpeningKernelSize = wx.SpinCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 20 )
		gSizer5.Add( self.m_spinCtrl_OpeningKernelSize, 0, wx.ALL, 5 )


		sbSizer9.Add( gSizer5, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer9, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer2.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel21, wx.ID_ANY, u"Input Image" ), wx.VERTICAL )

		self.m_bitmap_InputImage = wx.StaticBitmap( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 267,200 ), wx.BORDER_SUNKEN )
		sbSizer14.Add( self.m_bitmap_InputImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer15.Add( sbSizer14, 1, wx.EXPAND, 5 )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel21, wx.ID_ANY, u"Result Image" ), wx.VERTICAL )

		self.m_bitmap_ResultImage = wx.StaticBitmap( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 267,200 ), wx.BORDER_SUNKEN )
		sbSizer16.Add( self.m_bitmap_ResultImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer15.Add( sbSizer16, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.m_panel21.SetSizer( bSizer2 )
		self.m_panel21.Layout()
		bSizer2.Fit( self.m_panel21 )
		bSizer46.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_Run = wx.Button( self.m_panel3, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_Run.Enable( False )

		bSizer10.Add( self.m_button_Run, 0, wx.ALL, 5 )

		self.m_button_Back = wx.Button( self.m_panel3, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button_Back, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer10 )
		self.m_panel3.Layout()
		bSizer10.Fit( self.m_panel3 )
		bSizer46.Add( self.m_panel3, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel26.SetSizer( bSizer46 )
		self.m_panel26.Layout()
		bSizer46.Fit( self.m_panel26 )
		bSizer8.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Frame_WoodKnotLogicOnClose )
		self.m_button_Run.Bind( wx.EVT_BUTTON, self.m_button_RunOnButtonClick )
		self.m_button_Back.Bind( wx.EVT_BUTTON, self.m_button_BackOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Frame_WoodKnotLogicOnClose( self, event ):
		event.Skip()

	def m_button_RunOnButtonClick( self, event ):
		event.Skip()

	def m_button_BackOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Frame_MainMenu
###########################################################################

class Frame_MainMenu ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Image Processing Logic Tester", pos = wx.DefaultPosition, size = wx.Size( 288,214 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_LoadImage = wx.Button( self.m_panel18, wx.ID_ANY, u"Load Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button_LoadImage, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer29.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_WoodKnotLogic = wx.Button( self.m_panel18, wx.ID_ANY, u"Wood Knot Logic", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button_WoodKnotLogic, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer29.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_Help = wx.Button( self.m_panel18, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button_Help, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_About = wx.Button( self.m_panel18, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button_About, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel18.SetSizer( bSizer29 )
		self.m_panel18.Layout()
		bSizer29.Fit( self.m_panel18 )
		bSizer6.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Frame_MainMenuOnClose )
		self.m_button_LoadImage.Bind( wx.EVT_BUTTON, self.m_button_LoadImageOnButtonClick )
		self.m_button_WoodKnotLogic.Bind( wx.EVT_BUTTON, self.m_button_WoodKnotLogicOnButtonClick )
		self.m_button_Help.Bind( wx.EVT_BUTTON, self.m_button_HelpOnButtonClick )
		self.m_button_About.Bind( wx.EVT_BUTTON, self.m_button_AboutOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Frame_MainMenuOnClose( self, event ):
		event.Skip()

	def m_button_LoadImageOnButtonClick( self, event ):
		event.Skip()

	def m_button_WoodKnotLogicOnButtonClick( self, event ):
		event.Skip()

	def m_button_HelpOnButtonClick( self, event ):
		event.Skip()

	def m_button_AboutOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_Help
###########################################################################

class Dialog_Help ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 320,320 ), style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText28 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"This software is made to easily test various image processing logics.\n\nInstructions\n-------------\n\n1. Load the image for processing by pressing \"Load Image\".\n\n2. Choose the image processing logic to be conducted by pressing corresponding logic button.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer17.Add( self.m_staticText28, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer17 )
		self.m_panel7.Layout()
		bSizer17.Fit( self.m_panel7 )
		bSizer16.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel11 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_OK = wx.Button( self.m_panel11, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button_OK, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel11.SetSizer( bSizer24 )
		self.m_panel11.Layout()
		bSizer24.Fit( self.m_panel11 )
		bSizer23.Add( self.m_panel11, 1, wx.ALL, 5 )


		self.m_panel10.SetSizer( bSizer23 )
		self.m_panel10.Layout()
		bSizer23.Fit( self.m_panel10 )
		bSizer16.Add( self.m_panel10, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Dialog_HelpOnClose )
		self.m_button_OK.Bind( wx.EVT_BUTTON, self.m_button_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Dialog_HelpOnClose( self, event ):
		event.Skip()

	def m_button_OKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_About
###########################################################################

class Dialog_About ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 320,320 ), style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText28 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Made by Zarin!\n\nVer. 240825.1\n\nLicensed under BSD-3\n\n\"全てに意味があった。全てはこの時のために\"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer17.Add( self.m_staticText28, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer17 )
		self.m_panel7.Layout()
		bSizer17.Fit( self.m_panel7 )
		bSizer16.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel11 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_OK = wx.Button( self.m_panel11, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button_OK, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel11.SetSizer( bSizer24 )
		self.m_panel11.Layout()
		bSizer24.Fit( self.m_panel11 )
		bSizer23.Add( self.m_panel11, 1, wx.ALL, 5 )


		self.m_panel10.SetSizer( bSizer23 )
		self.m_panel10.Layout()
		bSizer23.Fit( self.m_panel10 )
		bSizer16.Add( self.m_panel10, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Dialog_AboutOnClose )
		self.m_button_OK.Bind( wx.EVT_BUTTON, self.m_button_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Dialog_AboutOnClose( self, event ):
		event.Skip()

	def m_button_OKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Frame_LoadImageNew
###########################################################################

class Frame_LoadImageNew ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 607,310 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel20 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel20, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Select image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer1.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.Hide()

		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.Hide()

		fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


		sbSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel20, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 267,200 ), wx.BORDER_SUNKEN )
		bSizer2.Add( self.m_bitmap2, 0, wx.ALL, 5 )


		self.m_panel20.SetSizer( bSizer2 )
		self.m_panel20.Layout()
		bSizer2.Fit( self.m_panel20 )
		bSizer42.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel29 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel28 = wx.Panel( self.m_panel29, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_OK = wx.Button( self.m_panel28, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button_OK, 0, wx.ALL, 5 )

		self.m_button_Cancel = wx.Button( self.m_panel28, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button_Cancel, 0, wx.ALL, 5 )


		self.m_panel28.SetSizer( bSizer10 )
		self.m_panel28.Layout()
		bSizer10.Fit( self.m_panel28 )
		bSizer59.Add( self.m_panel28, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel29.SetSizer( bSizer59 )
		self.m_panel29.Layout()
		bSizer59.Fit( self.m_panel29 )
		bSizer45.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer42.Add( bSizer45, 1, wx.EXPAND, 5 )


		self.m_panel23.SetSizer( bSizer42 )
		self.m_panel23.Layout()
		bSizer42.Fit( self.m_panel23 )
		bSizer46.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer46 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Frame_LoadImageNewOnClose )
		self.m_button_OK.Bind( wx.EVT_BUTTON, self.m_button_OKOnButtonClick )
		self.m_button_Cancel.Bind( wx.EVT_BUTTON, self.m_button_CancelOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Frame_LoadImageNewOnClose( self, event ):
		event.Skip()

	def m_button_OKOnButtonClick( self, event ):
		event.Skip()

	def m_button_CancelOnButtonClick( self, event ):
		event.Skip()


