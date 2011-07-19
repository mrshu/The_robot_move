#!/usr/bin/python

import wx

ID_UPLEFT = 1
ID_LEFT = 2
ID_DOWNLEFT = 3
ID_UP = 4
ID_CENTRE = 5
ID_DOWN = 6
ID_UPRIGHT = 7
ID_RIGHT = 8
ID_DOWNRIGHT = 9

class Arrows(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Arrows', size=(220, 230))

        

        self.InitUI()
        self.Centre()
        self.Show(True)

    def InitUI(self):
        menubar = wx.MenuBar()
        file = wx.Menu()
        quit = wx.MenuItem(file, 1, '&Quit\tCtrl+Q')
        file.AppendItem(quit)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)
        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)

        upleft = "icons/upleft.png"
        left = "icons/left.png"
        downleft = "icons/downleft.png"
        up = "icons/up.png"
        centre = "icons/centre.png"
        down = "icons/down.png"
        upright = "icons/upright.png"
        right = "icons/right.png"
        downright = "icons/downright.png"


        imageUPLEFT = wx.Image(upleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btnupleftClick, id= ID_UPLEFT)

        imageLEFT = wx.Image(left, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btnleftClick, id = ID_LEFT)
        
        imageDOWNLEFT = wx.Image(downleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btndownleftClick, id= ID_DOWNLEFT)
        
        imageUP = wx.Image(up, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btnupClick, id= ID_UP)
        
        imageCENTRE = wx.Image(centre, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btncentreClick, id= ID_CENTRE)
        
        imageDOWN = wx.Image(down, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btndownClick, id=ID_DOWN)
        
        imageUPRIGHT = wx.Image(upright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btnuprightClick, id = ID_UPRIGHT)
        
        imageRIGHT = wx.Image(right, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btnrightClick, id = ID_RIGHT)
        
        imageDOWNRIGHT = wx.Image(downright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.Bind(wx.EVT_BUTTON, self.btndownrightClick, id = ID_DOWNRIGHT)

        vbox = wx.BoxSizer(wx.VERTICAL)

        
       #wx.TextCtrl(self, style=wx.TE_RIGHT)
       #wx.TextCtrl(self, style=wx.TE_RIGHT)
       #wx.TextCtrl(self, style=wx.TE_RIGHT)

       #wx.TextCtrl(self, style=wx.TE_RIGHT)
        gs = wx.GridSizer(3, 3, 5, 5)

        gs.AddMany( [
            (wx.BitmapButton(self, id = ID_UPLEFT, bitmap=imageUPLEFT,
                pos=(5, 5), size = (imageUPLEFT.GetWidth()+5, imageUPLEFT.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_LEFT, bitmap=imageLEFT,
                pos=(5, 69), size = (imageLEFT.GetWidth()+5, imageLEFT.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_DOWNLEFT, bitmap=imageDOWNLEFT,
                pos=(5, 133), size = (imageDOWNLEFT.GetWidth()+5, imageDOWNLEFT.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_UP, bitmap=imageUP,
                pos=(69, 5), size = (imageUP.GetWidth()+5, imageUP.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_CENTRE, bitmap=imageCENTRE,
                pos=(69, 69), size = (imageCENTRE.GetWidth()+5, imageCENTRE.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_DOWN, bitmap=imageDOWN,
                pos=(69, 133), size = (imageDOWN.GetWidth()+5, imageDOWN.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_UPRIGHT, bitmap=imageUPRIGHT,
                pos=(133, 5), size = (imageUPRIGHT.GetWidth()+5, imageUPRIGHT.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_RIGHT, bitmap=imageRIGHT,
                pos=(133, 69), size = (imageRIGHT.GetWidth()+5, imageRIGHT.GetHeight()+5))),
            (wx.BitmapButton(self, id = ID_DOWNRIGHT, bitmap=imageDOWNRIGHT,
                pos=(133, 133), size = (imageDOWNRIGHT.GetWidth()+5, imageDOWNRIGHT.GetHeight()+5)))
            ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)
        

    def btnupleftClick(self,event):
        self.SetTitle("UPLEFT")

    def btnleftClick(self,event):
        self.SetTitle("LEFT")

    def btndownleftClick(self,event):
        self.SetTitle("DOWNLEFT")

    def btnupClick(self,event):
        self.SetTitle("UP")

    def btncentreClick(self,event):
        self.SetTitle("CENTRE")

    def btndownClick(self,event):
        self.SetTitle("DOWN")

    def btnuprightClick(self,event):
        self.SetTitle("UPRIGHT")

    def btnrightClick(self,event):
        self.SetTitle("RIGHT")

    def btndownrightClick(self,event):
        self.SetTitle("DOWNRIGHT")

    def OnQuit(self, event):
        self.Close()


 
app = wx.App()
Arrows(None, -1, 'Arrows')
app.MainLoop()
