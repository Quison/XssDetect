#_*_coding:utf-8_*_

import wx
from xss_detect_frame import XssDetectFrame

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
	xss_detect_app = XssDetectApp()
	xss_detect_app.MainLoop()

if __name__ == "__main__":
	main()
