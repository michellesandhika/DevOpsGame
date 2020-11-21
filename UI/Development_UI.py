import tkinter as tk
import tkinter.font as font

class Development(tk.Label):
    def __init__(self, parent, backend, nextButton):
        self.myFont = font.Font(size=15)
        tk.Label.__init__(self, parent, font=self.myFont, width=160, height=130, background="bisque", text="Development Finished! Please move on!")
        self.parent = parent
        self.backend = backend
        self.nextButton = nextButton
        self.myFont = font.Font(size=15)

        self.nextButton["state"] = tk.DISABLED

        self.backend.show_error()

        self.isFinish = True if len(self.backend.errorList) == 0 else False
        if(not(self.isFinish)):
            self.setBug()
        else:
            #show finish page
            self.nextButton["state"] = tk.NORMAL
        

    def setBug(self):
        selectedSolution = -1  
        current = self.backend.errorList[0]
        # feature name: current[0].feature_name
        # error message: current[1]["message"]
        # solutions: current[1]["solution"][i]["method"]

        self.label = tk.Label(self, text="A bug or situation happend during the development!\n We need your decision!\n\n  Feature:  "+current[0].feature_name + "\n   Error message:  "+ current[1]["message"],
            width=100, height=10, font=self.myFont,
            background="white")
        self.label.pack(anchor="w", padx=20, pady=5)

        self.button = []
        for i in range(len(current[1]["solution"])):
            self.button.append(tk.Button(self, text=current[1]["solution"][i]["method"],
                        width=30, height=2, font=self.myFont, bg="white",
                        command=lambda i=i:self.selectButton(i)))
            self.button[i].pack(anchor="e", padx=20, pady=5)


    def selectButton(self, i):
        self.label.destroy()
        for i in range(len(self.button)):
            self.button[i].destroy()

        self.isFinish = self.backend.solution_picked(i)

        if self.isFinish:
            #show finish page
            self.nextButton["state"] = tk.NORMAL
        else:
            self.setBug()