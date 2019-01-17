import wx

class WindowDragger:
    def __init__(self, window):
        self.window = window
        self.isDragStarted = False
        self.window.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.window.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.window.Bind(wx.EVT_MOTION, self.OnMouseMove)

    def OnLeftDown(self, evt):
        self.isDragStarted = True
        self.prevMousePos = evt.GetPosition()
        evt.Skip()

    def OnLeftUp(self, evt):
        self.isDragStarted = False
        evt.Skip()

    def OnMouseMove(self, evt):
        if self.isDragStarted:
            mousePos = evt.GetPosition()
            wndPos = self.window.GetPosition()
            self.window.Move(wndPos - (self.prevMousePos - mousePos))
        evt.Skip()