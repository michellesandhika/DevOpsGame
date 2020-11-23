import tkinter as tk
import tkinter.font as font

class Deployment(tk.Label):
    def __init__(self, parent, backend, nextButton):
        self.myFont = font.Font(size=15)
        tk.Label.__init__(self, parent, width=160, height=130, background="bisque")
        self.parent = parent
        self.backend = backend
        self.nextButton = nextButton

        for i in range(len(self.backend.featureSelected)):
            self.backend.new_failrate(self.backend.featureSelected[i])

        self.nextButton['state'] = tk.DISABLED

        self.guide = tk.Label(self, text="The final risks of failure:",
        width=80, height=3, font=self.myFont,
         background="white")
        self.guide.pack(anchor="w", padx=10, pady=5)

        self.deployLabels = []
        self.deployButtons = []
        self.letter = ['A', 'B', 'C']
        self.bText = ['feature A', 'feature B','feature C']
        self.selected = [False, False, False]
        for i in range(len(self.backend.featureSelected)):
            self.deployLabels.append(tk.Label(self, 
            text="Feature {}: {}\n                                              fail rate: {:3.0f}%".format(self.letter[i],self.backend.featureSelected[i].feature_name, self.backend.featureSelected[i].fail_rate*100),
            width=80, height=3, font=self.myFont,
            background="bisque"))

            self.deployButtons.append(tk.Button(self, text=self.bText[i],
                            width=28, height=2, font=self.myFont, bg="white",
                            command=lambda i=i:self.selectButton(i)))

            self.deployLabels[i].pack(anchor="w", padx=10, pady=5)

        self.choose = tk.Label(self, text="Which feature do you want to deploy (can choose multiple)",
            width=80, height=3, font=self.myFont,
                background="white")
        self.choose.pack(anchor="w", padx=10, pady=5)

        for i in range(len(self.backend.featureSelected)):
            self.deployButtons[i].pack(side=tk.LEFT)

    def selectButton(self, i):
        self.backend.feature_deployed(self.backend.featureSelected[i])
        self.selected[i] = not(self.selected[i])

        if self.selected[i]:
            self.deployButtons[i].configure(bg="#C8C3C2")
        else:
            self.deployButtons[i].configure(bg="white")


        if (self.selected.count(True) > 0):
            self.nextButton['state'] = tk.NORMAL
        else:
            self.nextButton['state'] = tk.DISABLED

       # print(self.backend.featureDeployed)
