import tkinter as tk

class Testing(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent, width=160, height=130, background="white", text="Testing")
        self.parent = parent