import os, glob, re, wx

class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs, size=(600,300))

        self.basicGUI()

    def basicGUI(self):

        # Menu Bar
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()

        ExitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Zamknij\tCtrl+Q')
        fileButton.Append(ExitItem)

        toolBar = self.CreateToolBar()

        menuBar.Append(fileButton, 'Plik')
    
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.Quit, ExitItem)
        # Menu Bar end
        
        wx.StaticText(panel, -1, 'Ścieżka folderu:', (5,0))
        self.pathFolder = wx.TextCtrl(panel, pos=(5, 25), size=(550, 18))

        wx.StaticText(panel, -1, 'Nazwa pliku do zmiany:', (5,50))
        self.nameOld = wx.TextCtrl(panel, pos=(5, 75), size=(550, 18))

        wx.StaticText(panel, -1, 'Nowa nazwa pliku:', (5,100))
        self.nameNew = wx.TextCtrl(panel, pos=(5, 125), size=(550, 18))    

        self.changeBtn = wx.Button(panel, label = 'Zmień nazwę', pos = (5, 150), size = (100,50))
        self.Bind(wx.EVT_BUTTON, self.changeName, self.changeBtn)
       
        self.SetTitle('Zmiana nazwy plików')
        self.Show(True)

    def Quit (self, e):
        self.Close()
      

    def changeName (self, event):

        pathFolder = self.pathFolder.GetValue()
        nameOld = self.nameOld.GetValue()
        nameNew = self.nameNew.GetValue()

        if nameOld != "" or nameNew != "":
            for f in os.listdir(pathFolder):
                os.rename(os.path.join(pathFolder, f), 
                          os.path.join(pathFolder, f.replace(nameOld, nameNew)))   

def main():
    app = wx.App()
    win = windowClass(None)
    win.Show()
    app.MainLoop()
    
main()
