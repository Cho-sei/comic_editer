import wx

class Paint:
	def __init__(self):

		slider = wx.Slider(self, style=wx.SL_HORIZONTAL, maxValue=50)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(slider)
		self.SetSizer(sizer)

		self.pen_width = 1
		slider.SetValue(1)

		slider.Bind(wx.EVT_SLIDER, self.OnSlide)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
		self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
		self.Bind(wx.EVT_MOTION, self.OnMotion)

		self.drag_flag = False
		self.spos = wx.Point(0, 0)
		self.ppos = wx.Point(0, 0)

	def OnLeftDown(self, event):
		self.spos = event.GetPosition()
		self.drag_flag = True

	def OnLeftUp(self, event):
		self.drag_flag = False

	def OnMotion(self, event):
		self.ppos = event.GetPosition()
		self.Refresh(False)

	def OnPaint(self, event):
		dc = wx.PaintDC(self)
		dc.SetPen(wx.Pen('black', self.pen_width))
		if self.drag_flag:
			dc.DrawLine(self.spos[0], self.spos[1], self.ppos[0], self.ppos[1])
		self.spos = self.ppos
	
	def OnSlide(self, event):
		choice = event.GetEventObject()
		self.pen_width = int(choice.GetValue())
		print(choice.GetValue())
