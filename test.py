import wx
import controlDragger

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Title', size=(200,150))
        panel = wx.Panel(self)
        childPanel = wx.Panel(panel, size=(30,30), pos=(50,10))
        childPanel.SetBackgroundColour('red')
        # Enable windows to drag.
        dragger = controlDragger.ControlDragger(childPanel)        

if __name__ == '__main__':
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()