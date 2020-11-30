import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter.messagebox import showinfo

from backend import Backend

from UI.Idea_UI import Idea
from UI.Development_UI import Development
from UI.Testing_UI import Testing
from UI.Deployment_UI import Deployment
from UI.Production_UI import Production
from UI.Result_UI import Result


class MainWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        
        ## show scnario popup

        self.master = master
        self.master.resizable(False, False)
        self.master.geometry("1300x720+0+0")
        self.master.configure(bg='bisque')

        self.backend = Backend()

        self.navi = NavigateFrame(self.master)
        self.navi.pack()
        self.nextButton = Next(self.master, self.nextPage)
        self.nextButton.pack(anchor = "s", side='right')
        self.window = WindowFrame(self.master)
        self.window.pack(side='left')
        self.window.pack_propagate(False)

        self.numPage = 6
        self.page = Idea(self.window, self.backend, self.nextButton)
        self.pageIndex = 0
        self.page.pack(side='left', padx=10, pady=10)

        ## displays popup message about airbnb scenario
        
        self.popup_showinfo()

    def nextPage(self):
        self.page.destroy()
        self.pageIndex = 0 if self.pageIndex == self.numPage-1 else self.pageIndex + 1
        
        if self.pageIndex == 0:
            self.navi.switch()
            self.page = Idea(self.window, self.backend, self.nextButton) 
        elif self.pageIndex == 1:
            self.navi.switch()
            self.page = Development(self.window, self.backend, self.nextButton) 
        elif self.pageIndex == 2:
            self.navi.switch()
            self.page = Testing(self.window, self.backend, self.nextButton) 
            self.master.iconify()
            self.master.deiconify()
        elif self.pageIndex == 3:
            self.navi.switch()
            self.page = Deployment(self.window, self.backend, self.nextButton) 
        elif self.pageIndex == 4:
            self.navi.switch()
            self.page = Production(self.window, self.backend) 
        elif self.pageIndex == 5:
            self.page = Result(self.window, self.backend) 

        

        self.page.pack(side='left', padx=10, pady=10)

    ## this function creates a popup window
    def popup_bonus(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        l = tk.Label(win, text="Input")
        l.grid(row=0, column=0)

        b = Button(win, text="Let's Begin", command=win.destroy)
        b.grid(row=1, column=0)

    ##define content of popup
    def popup_showinfo(self):
        showinfo("Scenario", "Airbnb has too much users and their servers does not hold, Therefore they want to swith to a different server!")

        
class NavigateFrame(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.get_box()
        self.boxes = [tk.Label(self, image=self.img_normal[i]) for i in range (0,5)]
        for i in range (0,5):
            self.boxes[i].grid(row=0, column=i) 

        self.current = 0
        self.boxes[self.current].configure(image=self.img_selected[self.current])

    def get_box(self):
        self.img_normal = [
            ImageTk.PhotoImage(Image.open("UI/img/idea.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/development.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/testing.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/deployment.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/production.JPG")),
            ]
        self.img_selected = [
            ImageTk.PhotoImage(Image.open("UI/img/idea_selected.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/development_selected.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/testing_selected.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/deployment_selected.JPG")),
            ImageTk.PhotoImage(Image.open("UI/img/production_selected.JPG")),
            ]

    def switch(self):
        self.boxes[self.current].configure(image=self.img_normal[self.current])
        self.current = 0 if self.current == 4 else self.current + 1
        self.boxes[self.current].configure(image=self.img_selected[self.current])
class WindowFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=1220, height=620, background="bisque")
        self.parent = parent

class Next(tk.Button):
    def __init__(self, parent, command):
        self.nextImg = ImageTk.PhotoImage(Image.open("UI/img/next.JPG"))
        tk.Button.__init__(self, parent, image=self.nextImg, command=command)
        self.parent = parent





if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    print("your screen's width x height = %d x %d (in pixels)" %(root.winfo_screenheight() , root.winfo_screenwidth() ))
    root.mainloop()