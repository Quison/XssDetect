# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import sys
import time
import threading

import wx
import wx.xrc
import wx.grid

reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(r"../comm")
sys.path.append(r"../spider")
sys.path.append(r"../check")

from file_helper import FileHelper
from common_util import CommonUtil
from spider_main import SpiderMain
from xss_check_main import CheckMain
from authentication_login import Login

###########################################################################
## Class XssDetectFrame
###########################################################################

class XssDetectFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Xss Detector", pos = wx.DefaultPosition, size = wx.Size( 800,750 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		#Fixed MainFrame's Size
		self.SetMaxSize(wx.Size(800,750))
		self.SetMinSize(wx.Size(800,750))
		#show frame at center of windows
		self.Center()

		main_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.logo_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		logo_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		#self.logo_bitmap = wx.StaticBitmap( self.logo_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		#logo_bSizer.Add( self.logo_bitmap, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		self.logo_bitmap = wx.StaticBitmap( self.logo_panel, bitmap=wx.Bitmap( u"images/logo.jpg", wx.BITMAP_TYPE_ANY ))
		logo_bSizer.Add( self.logo_bitmap, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.logo_panel.SetSizer( logo_bSizer )
		self.logo_panel.Layout()
		logo_bSizer.Fit( self.logo_panel )
		main_bSizer.Add( self.logo_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.setting_panel = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.thread_ctrl_panel = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		thread_ctrl_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self.thread_ctrl_panel, wx.ID_ANY, u"系统线程设置" ), wx.HORIZONTAL )
		
		self.spider_thread_num_staticText = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, u"爬虫线程数量（0~100）：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.spider_thread_num_staticText.Wrap( -1 )
		thread_ctrl_sbSizer.Add( self.spider_thread_num_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spider_thread_num_slider = wx.Slider( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, 10, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		thread_ctrl_sbSizer.Add( self.spider_thread_num_slider, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText_spider_unit = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		self.m_staticText_check_unit = wx.StaticText( thread_ctrl_sbSizer.GetStaticBox(), wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
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

		self.after_login_url_staticText = wx.StaticText( self.setting_login_info_ctrl_panel, wx.ID_ANY, u"after url：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.after_login_url_staticText.Wrap( -1 )
		settinglogin_bSizer.Add( self.after_login_url_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.after_login_url_textCtrl = wx.TextCtrl( self.setting_login_info_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		settinglogin_bSizer.Add( self.after_login_url_textCtrl, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.login_button = wx.Button( self.setting_login_info_ctrl_panel, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		settinglogin_bSizer.Add( self.login_button, 0, wx.ALL, 5 )
		
		
		self.setting_login_info_ctrl_panel.SetSizer( settinglogin_bSizer )
		self.setting_login_info_ctrl_panel.Layout()
		settinglogin_bSizer.Fit( self.setting_login_info_ctrl_panel )
		setting_login_info_sbSizer.Add( self.setting_login_info_ctrl_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_login_info_panel.SetSizer( setting_login_info_sbSizer )
		self.setting_login_info_panel.Layout()
		setting_login_info_sbSizer.Fit( self.setting_login_info_panel )
		setting_bSizer.Add( self.setting_login_info_panel, 5, wx.EXPAND |wx.ALL, 5 )
		
		self.setting_other_panel = wx.Panel( self.setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_other_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self.setting_other_panel, wx.ID_ANY, u"其他" ), wx.HORIZONTAL )
		
		self.setting_other_text_panel = wx.Panel( setting_other_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_other_text_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.other_text_panel = wx.Panel( self.setting_other_text_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		other_text_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.vercode_link_panel = wx.Panel( self.other_text_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		vercode_link_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.vercode_url_staticText = wx.StaticText( self.vercode_link_panel, wx.ID_ANY, u"验证码链接：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vercode_url_staticText.Wrap( -1 )
		vercode_link_bSizer.Add( self.vercode_url_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.vercode_url_textCtrl = wx.TextCtrl( self.vercode_link_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		vercode_link_bSizer.Add( self.vercode_url_textCtrl, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.vercode_link_panel.SetSizer( vercode_link_bSizer )
		self.vercode_link_panel.Layout()
		vercode_link_bSizer.Fit( self.vercode_link_panel )
		other_text_bSizer.Add( self.vercode_link_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.vercode_bitmap = wx.StaticBitmap( self.other_text_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		other_text_bSizer.Add( self.vercode_bitmap, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL
			, 5 )
		
		
		self.other_text_panel.SetSizer( other_text_bSizer )
		self.other_text_panel.Layout()
		other_text_bSizer.Fit( self.other_text_panel )
		setting_other_text_bSizer.Add( self.other_text_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.exclude_url_panel = wx.Panel( self.setting_other_text_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		exclude_url_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.exclude_url_staticText = wx.StaticText( self.exclude_url_panel, wx.ID_ANY, u"排除的URL（空格分隔）：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exclude_url_staticText.Wrap( -1 )
		exclude_url_bSizer.Add( self.exclude_url_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.exclude_url_textCtrl = wx.TextCtrl( self.exclude_url_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		exclude_url_bSizer.Add( self.exclude_url_textCtrl, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.exclude_url_panel.SetSizer( exclude_url_bSizer )
		self.exclude_url_panel.Layout()
		exclude_url_bSizer.Fit( self.exclude_url_panel )
		setting_other_text_bSizer.Add( self.exclude_url_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_other_text_panel.SetSizer( setting_other_text_bSizer )
		self.setting_other_text_panel.Layout()
		setting_other_text_bSizer.Fit( self.setting_other_text_panel )
		setting_other_sbSizer.Add( self.setting_other_text_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.save_info_panel = wx.Panel( setting_other_sbSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		save_info_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.save_info_staticText = wx.StaticText( self.save_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.save_info_staticText.Wrap( -1 )
		save_info_bSizer.Add( self.save_info_staticText, 1, wx.ALL, 5 )
		
		self.get_vercode_button = wx.Button( self.save_info_panel, wx.ID_ANY, u"获取验证码", wx.DefaultPosition, wx.DefaultSize, 0 )
		save_info_bSizer.Add( self.get_vercode_button, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.save_info_staticText1 = wx.StaticText( self.save_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.save_info_staticText1.Wrap( -1 )
		save_info_bSizer.Add( self.save_info_staticText1, 1, wx.ALL, 5 )
		
		self.save_info_button = wx.Button( self.save_info_panel, wx.ID_ANY, u"保存系统设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		save_info_bSizer.Add( self.save_info_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.save_info_panel.SetSizer( save_info_bSizer )
		self.save_info_panel.Layout()
		save_info_bSizer.Fit( self.save_info_panel )
		setting_other_sbSizer.Add( self.save_info_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_other_panel.SetSizer( setting_other_sbSizer )
		self.setting_other_panel.Layout()
		setting_other_sbSizer.Fit( self.setting_other_panel )
		setting_bSizer.Add( self.setting_other_panel, 3, wx.EXPAND |wx.ALL, 5 )
		
		
		self.setting_panel.SetSizer( setting_bSizer )
		self.setting_panel.Layout()
		setting_bSizer.Fit( self.setting_panel )
		self.m_notebook.AddPage( self.setting_panel, u"系统设置", True )
		self.spider_panel = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.spider_ctrl_panel = wx.Panel( self.spider_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_ctrl_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.seed_url_label = wx.StaticText( self.spider_ctrl_panel, wx.ID_ANY, u"种子连接：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.seed_url_label.Wrap( -1 )
		spider_ctrl_bSizer.Add( self.seed_url_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.seed_url_text = wx.TextCtrl( self.spider_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.seed_url_text, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.crawl_depth_staticText = wx.StaticText( self.spider_ctrl_panel, wx.ID_ANY, u"爬取深度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.crawl_depth_staticText.Wrap( -1 )
		spider_ctrl_bSizer.Add( self.crawl_depth_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.crawl_depth_textCtrl = wx.TextCtrl( self.spider_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.crawl_depth_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.start_crawling_button = wx.Button( self.spider_ctrl_panel, wx.ID_ANY, u"开始爬取", wx.DefaultPosition, wx.DefaultSize, 0 )
		spider_ctrl_bSizer.Add( self.start_crawling_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spider_ctrl_panel.SetSizer( spider_ctrl_bSizer )
		self.spider_ctrl_panel.Layout()
		spider_ctrl_bSizer.Fit( self.spider_ctrl_panel )
		spider_bSizer.Add( self.spider_ctrl_panel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.spider_show_panel = wx.Panel( self.spider_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spider_grid_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.spider_grid = wx.grid.Grid( self.spider_show_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.spider_grid.CreateGrid( 0, 4 )
		self.spider_grid.EnableEditing( True )
		self.spider_grid.EnableGridLines( True )
		self.spider_grid.EnableDragGridSize( False )
		self.spider_grid.SetMargins( 0, 0 )
		
		# Columns
		self.spider_grid.SetColSize( 0, 70 )
		self.spider_grid.SetColSize( 1, 450 )
		self.spider_grid.SetColSize( 2, 80 )
		self.spider_grid.SetColSize( 3, 40 )
		self.spider_grid.EnableDragColMove( False )
		self.spider_grid.EnableDragColSize( True )
		self.spider_grid.SetColLabelSize( 30 )
		self.spider_grid.SetColLabelValue( 0, u"线程名" )
		self.spider_grid.SetColLabelValue( 1, u"URL" )
		self.spider_grid.SetColLabelValue( 2, u"请求类型" )
		self.spider_grid.SetColLabelValue( 3, u"深度" )
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
		self.m_notebook.AddPage( self.spider_panel, u"网络爬虫", False )
		self.check_panel = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		check_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.check_ctrl_panel = wx.Panel( self.check_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		check_ctrl_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checking_staticText = wx.StaticText( self.check_ctrl_panel, wx.ID_ANY, u"正在检测：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checking_staticText.Wrap( -1 )
		check_ctrl_bSizer.Add( self.checking_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.checking_url_staticText = wx.StaticText( self.check_ctrl_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checking_url_staticText.Wrap( -1 )
		check_ctrl_bSizer.Add( self.checking_url_staticText, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.start_check_button = wx.Button( self.check_ctrl_panel, wx.ID_ANY, u"开始检测", wx.DefaultPosition, wx.DefaultSize, 0 )
		check_ctrl_bSizer.Add( self.start_check_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.check_ctrl_panel.SetSizer( check_ctrl_bSizer )
		self.check_ctrl_panel.Layout()
		check_ctrl_bSizer.Fit( self.check_ctrl_panel )
		check_bSizer.Add( self.check_ctrl_panel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.check_show_panel = wx.Panel( self.check_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		check_show_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.check_grid = wx.grid.Grid( self.check_show_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.check_grid.CreateGrid( 0, 4 )
		self.check_grid.EnableEditing( False )
		self.check_grid.EnableGridLines( True )
		self.check_grid.EnableDragGridSize( False )
		self.check_grid.SetMargins( 0, 0 )
		
		# Columns
		self.check_grid.SetColSize( 0, 80 )
		self.check_grid.SetColSize( 1, 75 )
		self.check_grid.SetColSize( 2, 400 )
		self.check_grid.SetColSize( 3, 80 )
		self.check_grid.EnableDragColMove( False )
		self.check_grid.EnableDragColSize( True )
		self.check_grid.SetColLabelSize( 30 )
		self.check_grid.SetColLabelValue( 0, u"线程名称" )
		self.check_grid.SetColLabelValue( 1, u"请求类型" )
		self.check_grid.SetColLabelValue( 2, u"URL" )
		self.check_grid.SetColLabelValue( 3, u"漏洞参数" )
		self.check_grid.SetColLabelValue( 4, wx.EmptyString )
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
		self.m_notebook.AddPage( self.check_panel, u"XSS 检测", False )
		
		main_bSizer.Add( self.m_notebook, 3, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( main_bSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.spider_thread_num_slider.Bind( wx.EVT_SCROLL, self.OnSpiderThreadNumScroll )
		self.check_thread_num_slider.Bind( wx.EVT_SCROLL, self.OnCheckThreadNumScroll )
		self.get_vercode_button.Bind( wx.EVT_BUTTON, self.OnGetVercodeButtonClick )
		self.login_button.Bind( wx.EVT_BUTTON, self.OnLoginButtonClick )
		self.save_info_button.Bind( wx.EVT_BUTTON, self.OnSaveSettingInfoButtonClick )
		self.start_crawling_button.Bind( wx.EVT_BUTTON, self.OnBeginCrawlingButtonClick )
		self.start_check_button.Bind( wx.EVT_BUTTON, self.OnBeginCheckButtonClick )

		# 填写初始配置信息
		self.init_setting();
		
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSpiderThreadNumScroll( self, event ):
		self.m_staticText_spider_unit.SetLabel(str(self.spider_thread_num_slider.GetValue()))
		event.Skip()
	
	def OnCheckThreadNumScroll( self, event ):
		self.m_staticText_check_unit.SetLabel(str(self.check_thread_num_slider.GetValue()))
		event.Skip()
	
	def OnGetVercodeButtonClick( self, event ):
		vercode_url = self.vercode_url_textCtrl.GetValue()
		# 如果为空
		if vercode_url == '':
			self.confirm_dialog(u"请填写验证码的链接！")
			return

		response_code = self.login.save_vercode(vercode_url)
		if response_code == 200:
			img = wx.Image("images/vercode.png", wx.BITMAP_TYPE_ANY)
			self.vercode_bitmap.SetBitmap(wx.BitmapFromImage(img))

		else:
			self.confirm_dialog(u"获取验证码错误！" + str(response_code))

		event.Skip()
	
	def OnLoginButtonClick( self, event ):
		# 将登录界面的信息保存到配置信息
		FileHelper.write_setting_info(self.get_setting_info())

		# 读取配置文件
		adict = FileHelper.read_setting_info()

		# 构造post的数据
		data = {}
		data[CommonUtil.get_dict_value(adict, "username_key")] = CommonUtil.get_dict_value(adict, "username_value")
		data[CommonUtil.get_dict_value(adict, "password_key")] = CommonUtil.get_dict_value(adict, "password_value")
		data[CommonUtil.get_dict_value(adict, "vercode_key")] = CommonUtil.get_dict_value(adict, "vercode_value")

		# 获取登陆连接
		login_url = CommonUtil.get_dict_value(adict, "login_url")
		after_login_url = CommonUtil.get_dict_value(adict, "after_login_url")

		print data
		# 一个login实例
		self.login = Login()

		if self.login_button.GetLabel() == u"登录":
			# 登录
			login_success,return_content = self.login.do_login(login_url, data, after_login_url)

			# 如果登录成功
			if login_success:
				self.cookie_textCtrl.SetValue(unicode(return_content))
				self.confirm_dialog(u"登录成功！")
				self.login_button.SetLabel(u"登出")
			else:
				self.confirm_dialog(unicode("登录失败" + "\n请重试！"))

		elif self.login_button.GetLabel == u"登出":
			print u"登出"
			self.login_button.SetLabel(u"登录")
			self.login.do_logout()


		FileHelper.write_setting_info(self.get_setting_info())

		event.Skip()
	
	def OnSaveSettingInfoButtonClick( self, event ):
		setting_info_dict = self.get_setting_info()
		FileHelper.write_setting_info(setting_info_dict)
		self.confirm_dialog(u"保存设置成功！")
		event.Skip()
	
	def OnBeginCrawlingButtonClick( self, event ):
		# 首先保存配置信息
		setting_info_dict = self.get_setting_info()
		FileHelper.write_setting_info(setting_info_dict)
		
		spider_thread_num = self.spider_thread_num_slider.GetValue()
		crawl_depth = self.crawl_depth_textCtrl.GetValue()
		# 获取爬虫需要的信息
		root_url = self.seed_url_text.GetValue()

		if self.start_crawling_button.GetLabel() == u"开始爬取":
			if spider_thread_num <= 0:
				self.confirm_dialog(u"请正确设置爬虫线程数量（测试推荐5~10）")
				return 

			# 如果种子连接为空提示
			if not root_url:
				self.confirm_dialog(u"请输入种子链接！")
				return
			# 判断是否符合条件
			elif not crawl_depth.isdigit():
				self.confirm_dialog(u"请正确设置爬虫的爬取深度（测试推荐2~4）")
				return 
			elif int(crawl_depth) <= 0:
				self.confirm_dialog(u"请正确设置爬虫的爬取深度（测试推荐2~4）")
				return

			self.start_crawling_button.SetLabel(u"暂停爬取")

			# 如果当前状态是终止检测的状态，清空表 ,重置爬取的url数据
			self.clear_spider_grid()

			self.spider_main = SpiderMain(self, root_url, int(spider_thread_num), int(crawl_depth), self.login.get_login_session())
			self.spider_main.crawling()

		elif self.start_crawling_button.GetLabel() == u"暂停爬取":
			self.start_crawling_button.SetLabel(u"开始爬取")
			# 暂停线程
			self.spider_main.stop()

		event.Skip()
	
	def OnBeginCheckButtonClick( self, event ):
		check_thread_num = self.check_thread_num_slider.GetValue()
		if self.start_check_button.GetLabel() == u"开始检测":
			self.start_check_button.SetLabel(u"暂停检测")
			# 如果当前状态是终止检测的状态，清空表
			self.clear_check_grid()
			self.check_main = CheckMain(self, check_thread_num, self.login.get_login_session())
			self.check_main.checking()


		elif self.start_check_button.GetLabel() == u"暂停检测":
			self.start_check_button.SetLabel(u"开始检测")
			self.check_main.stop()
			#do something

		event.Skip()

	def print_on_spider_grid(self, result_list):
		"""Print url on spider grid.
		
		Print already crawl url on grid.

		Args:
			url: a already crawl url string

		"""
		self.spider_grid.AppendRows()
		rows = self.spider_grid.GetNumberRows()
		for col in range(4):
			self.spider_grid.SetCellValue(rows-1, col, unicode(result_list[col]))

	def clear_spider_grid(self):
		"""
		Clear spider grid and romve rows.
		"""
		self.spider_grid.ClearGrid()
		rows = self.spider_grid.GetNumberRows()

		if rows > 0:
			self.spider_grid.DeleteRows(0, rows)

	def print_on_check_grid(self, result_list):
		"""Print result_list on spider grid.

		Args:
			result_list: a list contain xss_type, xss_url and xss_payload.
		"""
		self.check_grid.AppendRows()
		rows = self.check_grid.GetNumberRows()
		for col in range(4):
			self.check_grid.SetCellValue(rows-1, col, unicode(result_list[col]))

	def clear_check_grid(self):
		"""
		Clear check grid and romve rows.
		"""
		self.check_grid.ClearGrid()
		rows = self.check_grid.GetNumberRows()

		if rows > 0:
			self.check_grid.DeleteRows(0, rows)

	def set_reflect_cheking_url(self, reflect_checking_url):
		self.reflect_checking_url.SetLabel(reflect_checking_url)

	def set_stored_cheking_url(self, stored_checking_url):
		self.stored_checking_url.SetLabel(stored_checking_url)

	def get_setting_info(self):
		"""
		将配置信息格式化成键值对用于保存到配置文件中
		"""
		spider_thread_num = str(self.spider_thread_num_slider.GetValue())
		check_thread_num = str(self.check_thread_num_slider.GetValue())
		login_url = self.login_url_textCtrl.GetValue()
		cookie = self.cookie_textCtrl.GetValue()
		username_key = self.username_key_textCtrl.GetValue()
		username_value = self.username_value_textCtr.GetValue()
		password_key = self.password_key_textCtrl.GetValue()
		password_value = self.password_value_textCtr.GetValue()
		vercode_key = self.vercode_key_textCtrl.GetValue()
		vercode_value = self.vercode_value_textCtr.GetValue()
		vercode_url = self.vercode_url_textCtrl.GetValue()
		exclude_url = self.exclude_url_textCtrl.GetValue()
		after_login_url = self.after_login_url_textCtrl.GetValue()

		# 放到字典中
		setting_info_dict = {}
		setting_info_dict["spider_thread_num"] = spider_thread_num
		setting_info_dict["check_thread_num"] = check_thread_num
		setting_info_dict["login_url"] = login_url
		setting_info_dict["cookie"] = cookie
		setting_info_dict["username_key"] = username_key
		setting_info_dict["username_value"] = username_value
		setting_info_dict["password_key"] = password_key
		setting_info_dict["password_value"] = password_value
		setting_info_dict["vercode_key"] = vercode_key
		setting_info_dict["vercode_value"] = vercode_value
		setting_info_dict["vercode_url"] = vercode_url
		setting_info_dict["exclude_url"] = exclude_url
		setting_info_dict["after_login_url"] = after_login_url

		return setting_info_dict

	def confirm_dialog(self, message):
		dialog = wx.MessageDialog(None, message, u"Xss Detector", wx.OK)
		if dialog.ShowModal() == wx.ID_OK:
			dialog.Destroy()
	
	def init_setting(self):
		"""
		将配置文件中的信息写到界面上
		"""

		# 设置配置信息
		adict = FileHelper.read_setting_info()

		# 设置爬虫线程数
		spider_thread_num = CommonUtil.get_dict_value(adict, "spider_thread_num")
		if(spider_thread_num == ""):
			spider_thread_num = "10"
		self.spider_thread_num_slider.SetValue(int(spider_thread_num))
		self.m_staticText_spider_unit.SetLabel(spider_thread_num)

		#设置检测线程数
		check_thread_num = CommonUtil.get_dict_value(adict, "check_thread_num")
		if(check_thread_num == ""):
			check_thread_num = "10"

		self.check_thread_num_slider.SetValue(int(check_thread_num))
		self.m_staticText_check_unit.SetLabel(check_thread_num)
		self.login_url_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "login_url"))
		self.cookie_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "cookie"))
		self.username_key_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "username_key"))
		self.username_value_textCtr.SetValue(CommonUtil.get_dict_value(adict, "username_value"))
		self.password_key_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "password_key"))
		self.password_value_textCtr.SetValue(CommonUtil.get_dict_value(adict, "password_value"))
		self.vercode_key_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "vercode_key"))
		self.vercode_value_textCtr.SetValue(CommonUtil.get_dict_value(adict, "vercode_value"))
		self.vercode_url_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "vercode_url"))
		self.exclude_url_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "exclude_url"))
		self.after_login_url_textCtrl.SetValue(CommonUtil.get_dict_value(adict, "after_login_url"))
