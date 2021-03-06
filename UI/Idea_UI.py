import tkinter as tk
import tkinter.font as font

class Idea(tk.Label):
    def __init__(self, parent, backend, nextButton):
        tk.Label.__init__(self, parent, width=160, height=130, background="bisque")
        
        self.parent = parent
        self.backend = backend
        self.nextButton = nextButton
        self.myFont = font.Font(size=15)

        self.nextButton['state'] = tk.DISABLED

        self.label = tk.Label(self, text="Which features do you wish to deploy?\n (Please select at most 3)\n (the top is the biggest feature and the bottom is the smallest)",
        width=100, height=3, font=self.myFont,
         background="white")
        self.label.pack(anchor="nw", padx=20, pady=5)

        self.selected=[False for i in range (len(self.backend.returnFeatureClasses()))]
        self.button = []
        for i in range(len(self.backend.returnFeatureClasses())):
            self.button.append(tk.Button(self, text=self.backend.returnFeatureClasses()[i].feature_name,
                            width=80, height=2, font=self.myFont, bg="white",
                            command=lambda i=i:self.selectButton(i)))
            self.button[i].pack(anchor="w", padx=20, pady=5)

    def selectButton(self, i):
        for j in range (len(self.backend.returnFeatureClasses())):
            if self.button[j]["state"] == tk.DISABLED:
                self.button[j]["state"] = tk.NORMAL

        self.selected[i] = not(self.selected[i])

        if self.selected[i]:
            self.button[i].configure(bg="#C8C3C2")
        else:
            self.button[i].configure(bg="white")

        if self.selected.count(True) >= 3:
            for j in range (len(self.backend.returnFeatureClasses())):
                if self.selected[j] == False:
                    self.button[j]["state"] = tk.DISABLED

        if self.selected.count(True) > 0:
            self.nextButton['state'] = tk.NORMAL
        else:
            self.nextButton['state'] = tk.DISABLED

        self.backend.process_selected(i)

