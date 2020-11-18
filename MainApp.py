import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter.messagebox import showinfo

class MainWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)

        ## show scnario popup
        self.pack()



        self.master = master
        self.master.resizable(False, False)
        self.master.geometry("1300x720+0+0")

        self.navi = NavigateFrame(self.master)
        self.navi.pack()
        self.window = WindowFrame(self.master)
        self.window.pack(fill="both")
        self.window.pack_propagate(False)

        self.l1 = Label1(self.window)
        self.l1.pack(side=tk.TOP)

        self.nextButton = Next(self.window, self.nextPage)
        self.nextButton.pack(anchor = "e", side = "bottom")

        ## displays popup message about airbnb scenario
        popup_showinfo()
        self.pack()

    def nextPage(self):
        self.navi.switch()


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
            ImageTk.PhotoImage(Image.open("img/idea.JPG")),
            ImageTk.PhotoImage(Image.open("img/development.JPG")),
            ImageTk.PhotoImage(Image.open("img/testing.JPG")),
            ImageTk.PhotoImage(Image.open("img/deployment.JPG")),
            ImageTk.PhotoImage(Image.open("img/production.JPG")),
            ]
        self.img_selected = [
            ImageTk.PhotoImage(Image.open("img/idea_selected.JPG")),
            ImageTk.PhotoImage(Image.open("img/development_selected.JPG")),
            ImageTk.PhotoImage(Image.open("img/testing_selected.JPG")),
            ImageTk.PhotoImage(Image.open("img/deployment_selected.JPG")),
            ImageTk.PhotoImage(Image.open("img/production_selected.JPG")),
            ]

    def switch(self):
        self.boxes[self.current].configure(image=self.img_normal[self.current])
        self.current = 0 if self.current == 4 else self.current + 1
        self.boxes[self.current].configure(image=self.img_selected[self.current])
class WindowFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=1300, height=620, background="bisque")
        self.parent = parent


class Next(tk.Button):
    def __init__(self, parent, command):
        self.nextImg = ImageTk.PhotoImage(Image.open("img/next.JPG"))
        tk.Button.__init__(self, parent, image=self.nextImg, command=command)
        self.parent = parent


class Label1(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent, background="white", text="nothing yet")
        self.parent = parent


        
## this function creates a popup window
def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="Input")
    l.grid(row=0, column=0)

    b = Button(win, text="Let's Begin", command=win.destroy)
    b.grid(row=1, column=0)

##define content of popup
def popup_showinfo():
    showinfo("Scenario", "Airbnb has too much users and their servers does not hold, Therefore they want to swith to a different server!")


if __name__ == '__main__':
    root = tk.Tk()


    app = MainWindow(root)
    print("your screen's width x height = %d x %d (in pixels)" %(root.winfo_screenheight() , root.winfo_screenwidth() ))
    root.mainloop()