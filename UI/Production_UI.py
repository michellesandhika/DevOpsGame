import tkinter as tk

class Production(tk.Label):
    def __init__(self, parent, backend):
        tk.Label.__init__(self, parent, width=160, height=130, background="white", text="Production")
        self.parent = parent