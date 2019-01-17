import wx

class ControlDragger:
    def __init__(self, control):
        self.control = control
        self.drag_flag = False

        self.areaMAX = 100
        self.areaMIN = 20

        self.control.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.control.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.control.Bind(wx.EVT_MOTION, self.OnMotion)

    def OnLeftDown(self, evt):
        self.drag_flag = True
        self.control.CaptureMouse()
        self.prevMousePos = evt.GetPosition()
        print("click")
        evt.Skip()

    def OnLeftUp(self, evt):
        self.drag_flag = False
        self.control.ReleaseMouse()
        evt.Skip()

    def OnMotion(self, evt):
        if self.drag_flag:
            mousePos = evt.GetPosition()
            conPos = self.control.GetPosition()
            if conPos[0] < self.areaMAX and conPos[0] > self.areaMIN :
                self.control.Move(
                    conPos[0] - (self.prevMousePos[0] - mousePos[0]), conPos[1])

           # print(conPos, mousePos)
        evt.Skip()