import wx
import paint

"""
<memo>
アイコンの背景色：#FFF79D

"""

# アイコンのサイズ一括操作
ICON_SIZE = 50

# アイコン画像のリサイズ（正方形）
def scale_bitmap(img, width):
	image = wx.Image(img)
	image = image.Scale(width, width, wx.IMAGE_QUALITY_HIGH)
	result = wx.Bitmap(image)
	return result

# メニューボタンの定義
def setting_button(img, parent):
	input_file = "icon/" + img + ".png"
	image = wx.BitmapButton(
			parent, wx.ID_ANY, 
			scale_bitmap(input_file,ICON_SIZE), size=(ICON_SIZE,ICON_SIZE)
			)
	image.SetToolTip(img)
	return image

# メニューボタンのレイアウト
def button_layout(button_list):
	layout = wx.BoxSizer(wx.HORIZONTAL)
	for button in button_list:
		layout.Add(button, flag=wx.SHAPED | wx.ALIGN_BOTTOM | wx.ALL, border=10)
	return layout


class MainFrame(wx.Frame):
	# メインフレーム初期化
	def __init__(self):
		super().__init__(None, wx.ID_ANY, 'comic editer', size=(1500,900))

		Main_panel = wx.Panel(self, wx.ID_ANY)

		layout = wx.BoxSizer(wx.VERTICAL)
		layout.Add(MenuPanel(Main_panel), proportion=1, flag=wx.EXPAND)
		layout.Add(EditerPanel(Main_panel), proportion=7, flag=wx.EXPAND)
		Main_panel.SetSizer(layout)


class MenuPanel(wx.Panel):
	# 上部のメニュー部分
	def __init__(self, parent):
		super().__init__(parent, wx.ID_ANY)

		menu_notebook = wx.Notebook(self, wx.ID_ANY)

		menu_notebook.InsertPage(0, FileTab(menu_notebook), 'file')
		menu_notebook.InsertPage(1, EditTab(menu_notebook), 'edit')

		nb_layout = wx.BoxSizer(wx.VERTICAL)
		nb_layout.Add(menu_notebook, 1, wx.EXPAND)
		self.SetSizer(nb_layout)


class FileTab(wx.Panel):
	# メニュー内のファイル操作タブ
	def __init__(self, parent):
		super().__init__(parent, wx.ID_ANY)

		self.SetBackgroundColour('white')

		open_button = setting_button("open", self)
		save_button = setting_button("save", self)

		button_list = [open_button, save_button]

		self.SetSizer(button_layout(button_list))

class EditTab(wx.Panel):
	# メニュー内の編集タブ
	def __init__(self, parent):
		super().__init__(parent, wx.ID_ANY)

		self.SetBackgroundColour('white')

		undo_button = setting_button("undo", self)
		redo_button = setting_button("redo", self)
		pen_button = setting_button("pen", self)
		beta_button = setting_button("beta", self)
		line_button = setting_button("line", self)
		erase_button = setting_button("erase", self)

		button_list = [undo_button, redo_button, pen_button, beta_button,
			line_button, erase_button]

		self.SetSizer(button_layout(button_list))


class EditerPanel(wx.Panel):
	# メインの表示、編集部分
	def __init__(self, parent):
		super().__init__(parent, wx.ID_ANY)

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
		width = event.GetEventObject()
		self.pen_width = int(width.GetValue())



if __name__ == '__main__':
	app = wx.App()

	frame = MainFrame()

	frame.Show()
	frame.Centre()

	app.MainLoop()
