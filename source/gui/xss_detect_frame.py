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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Xss Detector", pos = wx.DefaultPosition, size = wx.Size( 799,703 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		main_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.logo_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		logo_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.logo_bitmap = wx.StaticBitmap( self.logo_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		logo_bSizer.Add( self.logo_bitmap, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.logo_panel.SetSizer( logo_bSizer )
		self.logo_panel.Layout()
		logo_bSizer.Fit( self.logo_panel )
		main_bSizer.Add( self.logo_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.setting_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.thread_ctrl_panel = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		thread_ctrl_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self.thread_ctrl_panel, wx.ID_ANY, u"系统线程设置" ), wx.HORIZONTAL )
		
		self.spider_thread_num_staticText = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, u"爬虫线程数量（0~100）：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spider_thread_num_staticText.Wrap( -1 )
		thread_ctrl_sbSizer.Add( self.spider_thread_num_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spider_thread_num_slider = wx.Slider( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		thread_ctrl_sbSizer.Add( self.spider_thread_num_slider, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText_spider_unit = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_spider_unit.Wrap( -1 )
		thread_ctrl_sbSizer.Add( self.m_staticText_spider_unit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText_space = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, u"df" )
		self.m_staticText_space.Wrap( -1 )
		thread_ctrl_sbSizer.Add( self.m_staticText_space, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.check_thread_num_staticText = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, u"检测线程数量（0~100）：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_thread_num_staticText.Wrap( -1 )
		thread_ctrl_sbSizer.Add( self.check_thread_num_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.check_thread_num_slider = wx.Slider( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		thread_ctrl_sbSizer.Add( self.check_thread_num_slider, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText_check_unit = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_check_unit.Wrap( -1 )
		thread_ctrl_sbSizer.Add( self.m_staticText_check_unit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.thread_ctrl_panel.SetSizer( thread_ctrl_sbSizer )
		self.thread_ctrl_panel.Layout()
		thread_ctrl_sbSizer.Fit( self.thread_ctrl_panel )
		setting_bSizer.Add( self.thread_ctrl_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.setting_login_info_panel = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_login_info_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self.setting_login_info_panel, wx.ID_ANY, u"HTTP授权信息" ), wx.VERTICAL )
		
		self.setting_cookie_panel = wx.Panel( setting_login_info_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_cookie_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.login_url_staticText = wx.StaticText( self.setting_cookie_panel, wx.ID_ANY, u"登录链接：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login_url_staticText.Wrap( -1 )
		setting_cookie_bSizer.Add( self.login_url_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.login_url_textCtrl = wx.TextCtrl( self.setting_cookie_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_cookie_bSizer.Add( self.login_url_textCtrl, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.cookie_staticText = wx.StaticText( self.setting_cookie_panel, wx.ID_ANY, u"Cookie：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cookie_staticText.Wrap( -1 )
		setting_cookie_bSizer.Add( self.cookie_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.cookie_textCtrl = wx.TextCtrl( self.setting_cookie_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_cookie_bSizer.Add( self.cookie_textCtrl, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.vercode_staticText = wx.StaticText( self.setting_cookie_panel, wx.ID_ANY, u"验证码链接：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vercode_staticText.Wrap( -1 )
		setting_cookie_bSizer.Add( self.vercode_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.vercode_textCtrl = wx.TextCtrl( self.setting_cookie_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_cookie_bSizer.Add( self.vercode_textCtrl, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.setting_cookie_panel.SetSizer( setting_cookie_bSizer )
		self.setting_cookie_panel.Layout()
		setting_cookie_bSizer.Fit( self.setting_cookie_panel )
		setting_login_info_sbSizer.Add( self.setting_cookie_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.setting_username_panel = wx.Panel( setting_login_info_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_username_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.username_key_staticText = wx.StaticText( self.setting_username_panel, wx.ID_ANY, u"username key：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_key_staticText.Wrap( -1 )
		setting_username_bSizer.Add( self.username_key_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.username_key_textCtrl = wx.TextCtrl( self.setting_username_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_username_bSizer.Add( self.username_key_textCtrl, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.username_value_staticText1 = wx.StaticText( self.setting_username_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_value_staticText1.Wrap( -1 )
		setting_username_bSizer.Add( self.username_value_staticText1, 1, wx.ALL, 5 )
		
		self.username_value_staticText = wx.StaticText( self.setting_username_panel, wx.ID_ANY, u"username value：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_value_staticText.Wrap( -1 )
		setting_username_bSizer.Add( self.username_value_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.username_value_textCtr = wx.TextCtrl( self.setting_username_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_username_bSizer.Add( self.username_value_textCtr, 3, wx.ALL, 5 )
		
		
		self.setting_username_panel.SetSizer( setting_username_bSizer )
		self.setting_username_panel.Layout()
		setting_username_bSizer.Fit( self.setting_username_panel )
		setting_login_info_sbSizer.Add( self.setting_username_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.setting_password_panel = wx.Panel( setting_login_info_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_username_bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.password_key_staticText = wx.StaticText( self.setting_password_panel, wx.ID_ANY, u"password key：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password_key_staticText.Wrap( -1 )
		setting_username_bSizer1.Add( self.password_key_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.password_key_textCtrl = wx.TextCtrl( self.setting_password_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_username_bSizer1.Add( self.password_key_textCtrl, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.username_value_staticText11 = wx.StaticText( self.setting_password_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_value_staticText11.Wrap( -1 )
		setting_username_bSizer1.Add( self.username_value_staticText11, 1, wx.ALL, 5 )
		
		self.password_value_staticText = wx.StaticText( self.setting_password_panel, wx.ID_ANY, u"password value：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password_value_staticText.Wrap( -1 )
		setting_username_bSizer1.Add( self.password_value_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.password_value_textCtr = wx.TextCtrl( self.setting_password_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_username_bSizer1.Add( self.password_value_textCtr, 3, wx.ALL, 5 )
		
		
		self.setting_password_panel.SetSizer( setting_username_bSizer1 )
		self.setting_password_panel.Layout()
		setting_username_bSizer1.Fit( self.setting_password_panel )
		setting_login_info_sbSizer.Add( self.setting_password_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.setting_vercode_panel = wx.Panel( setting_login_info_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_username_bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.vercode_key_staticText = wx.StaticText( self.setting_vercode_panel, wx.ID_ANY, u"vercode key：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vercode_key_staticText.Wrap( -1 )
		setting_username_bSizer11.Add( self.vercode_key_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.vercode_key_textCtrl = wx.TextCtrl( self.setting_vercode_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_username_bSizer11.Add( self.vercode_key_textCtrl, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.username_value_staticText111 = wx.StaticText( self.setting_vercode_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_value_staticText111.Wrap( -1 )
		setting_username_bSizer11.Add( self.username_value_staticText111, 1, wx.ALL, 5 )
		
		self.vercode_value_staticText = wx.StaticText( self.setting_vercode_panel, wx.ID_ANY, u"vercode value：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vercode_value_staticText.Wrap( -1 )
		setting_username_bSizer11.Add( self.vercode_value_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.vercode_value_textCtr = wx.TextCtrl( self.setting_vercode_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_username_bSizer11.Add( self.vercode_value_textCtr, 3, wx.ALL, 5 )
		
		
		self.setting_vercode_panel.SetSizer( setting_username_bSizer11 )
		self.setting_vercode_panel.Layout()
		setting_username_bSizer11.Fit( self.setting_vercode_panel )
		setting_login_info_sbSizer.Add( self.setting_vercode_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.setting_login_info_ctrl_panel = wx.Panel( setting_login_info_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		settinglogin_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText41 = wx.StaticText( self.setting_login_info_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		settinglogin_bSizer.Add( self.m_staticText41, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.vercode_bitmap = wx.StaticBitmap( self.setting_login_info_ctrl_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		settinglogin_bSizer.Add( self.vercode_bitmap, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText42 = wx.StaticText( self.setting_login_info_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		settinglogin_bSizer.Add( self.m_staticText42, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.get_vercode_button = wx.Button( self.setting_login_info_ctrl_panel, wx.ID_ANY, u"获取验证码", wx.DefaultPosition, wx.DefaultSize, 0 )
		settinglogin_bSizer.Add( self.get_vercode_button, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.login_button = wx.Button( self.setting_login_info_ctrl_panel, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		settinglogin_bSizer.Add( self.login_button, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.setting_login_info_ctrl_panel.SetSizer( settinglogin_bSizer )
		self.setting_login_info_ctrl_panel.Layout()
		settinglogin_bSizer.Fit( self.setting_login_info_ctrl_panel )
		setting_login_info_sbSizer.Add( self.setting_login_info_ctrl_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_login_info_panel.SetSizer( setting_login_info_sbSizer )
		self.setting_login_info_panel.Layout()
		setting_login_info_sbSizer.Fit( self.setting_login_info_panel )
		setting_bSizer.Add( self.setting_login_info_panel, 5, wx.EXPAND |wx.ALL, 5 )
		
		self.setting_payload_panel = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_payload_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self.setting_payload_panel, wx.ID_ANY, u"自定义信息" ), wx.HORIZONTAL )
		
		self.setting_payload_text_panel = wx.Panel( setting_payload_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_payload_text_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.payload_text_panel = wx.Panel( self.setting_payload_text_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		payload_text_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.payload_staticText = wx.StaticText( self.payload_text_panel, wx.ID_ANY, u"自定义向量：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.payload_staticText.Wrap( -1 )
		payload_text_bSizer.Add( self.payload_staticText, 0, wx.ALL, 5 )
		
		payload_listBoxChoices = []
		self.payload_listBox = wx.ListBox( self.payload_text_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, payload_listBoxChoices, 0 )
		payload_text_bSizer.Add( self.payload_listBox, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.payload_text_panel.SetSizer( payload_text_bSizer )
		self.payload_text_panel.Layout()
		payload_text_bSizer.Fit( self.payload_text_panel )
		setting_payload_text_bSizer.Add( self.payload_text_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.exclude_url_panel = wx.Panel( self.setting_payload_text_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		exclude_url_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.exclude_url_staticText = wx.StaticText( self.exclude_url_panel, wx.ID_ANY, u"排除的URL：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exclude_url_staticText.Wrap( -1 )
		exclude_url_bSizer.Add( self.exclude_url_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.exclude_url_textCtrl = wx.TextCtrl( self.exclude_url_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		exclude_url_bSizer.Add( self.exclude_url_textCtrl, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.exclude_url_panel.SetSizer( exclude_url_bSizer )
		self.exclude_url_panel.Layout()
		exclude_url_bSizer.Fit( self.exclude_url_panel )
		setting_payload_text_bSizer.Add( self.exclude_url_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_payload_text_panel.SetSizer( setting_payload_text_bSizer )
		self.setting_payload_text_panel.Layout()
		setting_payload_text_bSizer.Fit( self.setting_payload_text_panel )
		setting_payload_sbSizer.Add( self.setting_payload_text_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.save_info_panel = wx.Panel( setting_payload_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		save_info_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.save_info_staticText = wx.StaticText( self.save_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.save_info_staticText.Wrap( -1 )
		save_info_bSizer.Add( self.save_info_staticText, 1, wx.ALL, 5 )
		
		self.save_payload_button = wx.Button( self.save_info_panel, wx.ID_ANY, u"添加PAYLOAD", wx.DefaultPosition, wx.DefaultSize, 0 )
		save_info_bSizer.Add( self.save_payload_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.save_info_staticText1 = wx.StaticText( self.save_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.save_info_staticText1.Wrap( -1 )
		save_info_bSizer.Add( self.save_info_staticText1, 1, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.save_info_panel, wx.ID_ANY, u"保存系统设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		save_info_bSizer.Add( self.m_button6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.save_info_panel.SetSizer( save_info_bSizer )
		self.save_info_panel.Layout()
		save_info_bSizer.Fit( self.save_info_panel )
		setting_payload_sbSizer.Add( self.save_info_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_payload_panel.SetSizer( setting_payload_sbSizer )
		self.setting_payload_panel.Layout()
		setting_payload_sbSizer.Fit( self.setting_payload_panel )
		setting_bSizer.Add( self.setting_payload_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_panel.SetSizer( setting_bSizer )
		self.setting_panel.Layout()
		setting_bSizer.Fit( self.setting_panel )
		self.m_notebook4.AddPage( self.setting_panel, u"系统设置", True )
		self.spider_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.spider_ctrl_panel = wx.Panel( self.spider_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_ctrl_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.seed_url_label = wx.StaticText( self.spider_ctrl_panel, wx.ID_ANY, u"种子连接：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.seed_url_label.Wrap( -1 )
		spider_ctrl_bSizer.Add( self.seed_url_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.seed_url_text = wx.TextCtrl( self.spider_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.seed_url_text, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.start_crawler_button = wx.Button( self.spider_ctrl_panel, wx.ID_ANY, u"开始爬取", wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.start_crawler_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.end_crawler_button = wx.Button( self.spider_ctrl_panel, wx.ID_ANY, u"终止爬取", wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.end_crawler_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
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
		self.spider_grid.SetColSize( 0, 666 )
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
		self.m_notebook4.AddPage( self.spider_panel, u"网络爬虫", False )
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
		
		self.start_check_button = wx.Button( self.ctrl_panel, wx.ID_ANY, u"开始检测", wx.DefaultPosition, wx.DefaultSize, 0 )
		ctrl_bSizer9.Add( self.start_check_button, 0, wx.ALL, 5 )
		
		self.end_check_button = wx.Button( self.ctrl_panel, wx.ID_ANY, u"终止检测", wx.DefaultPosition, wx.DefaultSize, 0 )
		ctrl_bSizer9.Add( self.end_check_button, 0, wx.ALL, 5 )
		
		
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
		self.check_grid.EnableEditing( False )
		self.check_grid.EnableGridLines( True )
		self.check_grid.EnableDragGridSize( False )
		self.check_grid.SetMargins( 0, 0 )
		
		# Columns
		self.check_grid.SetColSize( 0, 80 )
		self.check_grid.SetColSize( 1, 422 )
		self.check_grid.SetColSize( 2, 163 )
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
		
		main_bSizer.Add( self.m_notebook4, 3, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( main_bSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
