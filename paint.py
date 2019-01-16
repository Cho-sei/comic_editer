import wx


class MainFrame(wx.Frame):
	def __init__(self):
		super().__init__(None, wx.ID_ANY, 'test', size=(300,300))

		self.SetBackgroundColour('white')

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
		self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
		self.Bind(wx.EVT_MOTION, self.OnMotion)

		self.drag_flag = False

	def OnLeftDown(self, event):
		self.spos = event.GetPosition()
		self.drag_flag = True

	def OnLeftUp(self, event):
		self.drag_flag = False

	def OnMotion(self, event):
		self.ppos = event.GetPosition()

	def OnPaint(self, event):
		dc = wx.PaintDC(self)
		if self.drag_flag:
			dc.DrawLine(self.spos[0], self.spos[1], self.ppos[0], self.ppos[1])
		self.Refresh(False)

if __name__ == '__main__':
	app = wx.App()

	frame = MainFrame()

	frame.Show()
	frame.Centre()

	app.MainLoop()