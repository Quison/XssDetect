# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class XssDetectFrame
###########################################################################

class XssDetectFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Xss Detector", pos = wx.DefaultPosition, size = wx.Size( 750,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		main_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.logo_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		logo_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.logo_bitmap = wx.StaticBitmap( self.logo_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		logo_bSizer.Add( self.logo_bitmap, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.logo_panel.SetSizer( logo_bSizer )
		self.logo_panel.Layout()
		logo_bSizer.Fit( self.logo_panel )
		main_bSizer.Add( self.logo_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spider_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.spider_ctrl_panel = wx.Panel( self.spider_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_ctrl_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.seed_url_label = wx.StaticText( self.spider_ctrl_panel, wx.ID_ANY, u"种子连接：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.seed_url_label.Wrap( -1 )
		spider_ctrl_bSizer.Add( self.seed_url_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.seed_url_text = wx.TextCtrl( self.spider_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.seed_url_text, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.start_crawler_btn = wx.Button( self.spider_ctrl_panel, wx.ID_ANY, u"开始爬取", wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.start_crawler_btn, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_button = wx.Button( self.spider_ctrl_panel, wx.ID_ANY, u"终止爬取", wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.m_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.spider_ctrl_panel.SetSizer( spider_ctrl_bSizer )
		self.spider_ctrl_panel.Layout()
		spider_ctrl_bSizer.Fit( self.spider_ctrl_panel )
		spider_bSizer.Add( self.spider_ctrl_panel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.spider_show_panel = wx.Panel( self.spider_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_grid_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.spider_grid = wx.grid.Grid( self.spider_show_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.spider_grid.CreateGrid( 10, 1 )
		self.spider_grid.EnableEditing( True )
		self.spider_grid.EnableGridLines( True )
		self.spider_grid.EnableDragGridSize( False )
		self.spider_grid.SetMargins( 0, 0 )
		
		# Columns
		self.spider_grid.SetColSize( 0, 607 )
		self.spider_grid.EnableDragColMove( False )
		self.spider_grid.EnableDragColSize( True )
		self.spider_grid.SetColLabelSize( 30 )
		self.spider_grid.SetColLabelValue( 0, u"已爬取的URL" )
		self.spider_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.spider_grid.EnableDragRowSize( True )
		self.spider_grid.SetRowLabelSize( 80 )
		self.spider_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.spider_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		spider_grid_bSizer.Add( self.spider_grid, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.spider_show_panel.SetSizer( spider_grid_bSizer )
		self.spider_show_panel.Layout()
		spider_grid_bSizer.Fit( self.spider_show_panel )
		spider_bSizer.Add( self.spider_show_panel, 6, wx.EXPAND |wx.ALL, 5 )
		
		
		self.spider_panel.SetSizer( spider_bSizer )
		self.spider_panel.Layout()
		spider_bSizer.Fit( self.spider_panel )
		self.m_notebook4.AddPage( self.spider_panel, u"网络爬虫", True )
		self.check_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		check_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.check_ctrl_panel = wx.Panel( self.check_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		check_ctrl_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checking_panel = wx.Panel( self.check_ctrl_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		checking_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.reflect_check_panel = wx.Panel( self.checking_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		reflected_check_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.reflect_check_staticText = wx.StaticText( self.reflect_check_panel, wx.ID_ANY, u"反射型XSS检测：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reflect_check_staticText.Wrap( -1 )
		reflected_check_bSizer.Add( self.reflect_check_staticText, 0, wx.ALL, 5 )
		
		self.reflect_checking_url = wx.StaticText( self.reflect_check_panel, wx.ID_ANY, u"www.baidu.com..", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reflect_checking_url.Wrap( -1 )
		reflected_check_bSizer.Add( self.reflect_checking_url, 0, wx.ALL, 5 )
		
		
		self.reflect_check_panel.SetSizer( reflected_check_bSizer )
		self.reflect_check_panel.Layout()
		reflected_check_bSizer.Fit( self.reflect_check_panel )
		checking_bSizer.Add( self.reflect_check_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.stored_check_panel = wx.Panel( self.checking_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		stored_check_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stored_check_staticText = wx.StaticText( self.stored_check_panel, wx.ID_ANY, u"存储型XSS检测：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stored_check_staticText.Wrap( -1 )
		stored_check_bSizer.Add( self.stored_check_staticText, 0, wx.ALL, 5 )
		
		self.stored_checking_url = wx.StaticText( self.stored_check_panel, wx.ID_ANY, u"www.baidu.com..", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stored_checking_url.Wrap( -1 )
		stored_check_bSizer.Add( self.stored_checking_url, 0, wx.ALL, 5 )
		
		
		self.stored_check_panel.SetSizer( stored_check_bSizer )
		self.stored_check_panel.Layout()
		stored_check_bSizer.Fit( self.stored_check_panel )
		checking_bSizer.Add( self.stored_check_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.checking_panel.SetSizer( checking_bSizer )
		self.checking_panel.Layout()
		checking_bSizer.Fit( self.checking_panel )
		check_ctrl_bSizer.Add( self.checking_panel, 6, wx.EXPAND |wx.ALL, 5 )
		
		self.ctrl_panel = wx.Panel( self.check_ctrl_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		ctrl_bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.start_check_btn = wx.Button( self.ctrl_panel, wx.ID_ANY, u"开始检测", wx.DefaultPosition, wx.DefaultSize, 0 )
		ctrl_bSizer9.Add( self.start_check_btn, 0, wx.ALL, 5 )
		
		self.end_check_btn = wx.Button( self.ctrl_panel, wx.ID_ANY, u"终止检测", wx.DefaultPosition, wx.DefaultSize, 0 )
		ctrl_bSizer9.Add( self.end_check_btn, 0, wx.ALL, 5 )
		
		
		self.ctrl_panel.SetSizer( ctrl_bSizer9 )
		self.ctrl_panel.Layout()
		ctrl_bSizer9.Fit( self.ctrl_panel )
		check_ctrl_bSizer.Add( self.ctrl_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.check_ctrl_panel.SetSizer( check_ctrl_bSizer )
		self.check_ctrl_panel.Layout()
		check_ctrl_bSizer.Fit( self.check_ctrl_panel )
		check_bSizer.Add( self.check_ctrl_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.check_show_panel = wx.Panel( self.check_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		check_show_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.check_grid = wx.grid.Grid( self.check_show_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.check_grid.CreateGrid( 10, 3 )
		self.check_grid.EnableEditing( True )
		self.check_grid.EnableGridLines( True )
		self.check_grid.EnableDragGridSize( False )
		self.check_grid.SetMargins( 0, 0 )
		
		# Columns
		self.check_grid.SetColSize( 0, 80 )
		self.check_grid.SetColSize( 1, 423 )
		self.check_grid.SetColSize( 2, 106 )
		self.check_grid.EnableDragColMove( False )
		self.check_grid.EnableDragColSize( True )
		self.check_grid.SetColLabelSize( 30 )
		self.check_grid.SetColLabelValue( 0, u"XSS漏洞类型" )
		self.check_grid.SetColLabelValue( 1, u"存在漏洞的URL" )
		self.check_grid.SetColLabelValue( 2, u"PAYLOAD" )
		self.check_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.check_grid.EnableDragRowSize( True )
		self.check_grid.SetRowLabelSize( 80 )
		self.check_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.check_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		check_show_bSizer.Add( self.check_grid, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.check_show_panel.SetSizer( check_show_bSizer )
		self.check_show_panel.Layout()
		check_show_bSizer.Fit( self.check_show_panel )
		check_bSizer.Add( self.check_show_panel, 4, wx.EXPAND |wx.ALL, 5 )
		
		
		self.check_panel.SetSizer( check_bSizer )
		self.check_panel.Layout()
		check_bSizer.Fit( self.check_panel )
		self.m_notebook4.AddPage( self.check_panel, u"XSS 检测", False )
		self.setting_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.thread_ctrl_panel = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spider_thread_num_staticText = wx.StaticText( self.thread_ctrl_panel, wx.ID_ANY, u"爬虫线程数量（0~100）：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spider_thread_num_staticText.Wrap( -1 )
		bSizer14.Add( self.spider_thread_num_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spider_thread_num_slider = wx.Slider( self.thread_ctrl_panel, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer14.Add( self.spider_thread_num_slider, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText_spider_unit = wx.StaticText( self.thread_ctrl_panel, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_spider_unit.Wrap( -1 )
		bSizer14.Add( self.m_staticText_spider_unit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText_space = wx.StaticText( self.thread_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, u"df" )
		self.m_staticText_space.Wrap( -1 )
		bSizer14.Add( self.m_staticText_space, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.check_thread_num_staticText = wx.StaticText( self.thread_ctrl_panel, wx.ID_ANY, u"检测线程数量（0~100）：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_thread_num_staticText.Wrap( -1 )
		bSizer14.Add( self.check_thread_num_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.check_thread_num_slider = wx.Slider( self.thread_ctrl_panel, wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer14.Add( self.check_thread_num_slider, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText_check_unit = wx.StaticText( self.thread_ctrl_panel, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_check_unit.Wrap( -1 )
		bSizer14.Add( self.m_staticText_check_unit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.thread_ctrl_panel.SetSizer( bSizer14 )
		self.thread_ctrl_panel.Layout()
		bSizer14.Fit( self.thread_ctrl_panel )
		setting_bSizer.Add( self.thread_ctrl_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel14 = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_bSizer.Add( self.m_panel14, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel15 = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_bSizer.Add( self.m_panel15, 3, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_panel.SetSizer( setting_bSizer )
		self.setting_panel.Layout()
		setting_bSizer.Fit( self.setting_panel )
		self.m_notebook4.AddPage( self.setting_panel, u"系统设置", False )
		
		main_bSizer.Add( self.m_notebook4, 5, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( main_bSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

class XssDetectApp(wx.App):
	"""
	XssDetec application
	"""
	def OnInit(self):
		self.frame = XssDetectFrame(None)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

def main():
	"""
	main function of program
	"""
	app = XssDetectApp()
	app.MainLoop()

if __name__ == "__main__":
	main()

	