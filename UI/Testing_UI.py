import tkinter as tk
import tkinter.font as font

class Testing(tk.Label):
    def __init__(self, parent, backend, nextButton):
        self.myFont = font.Font(size=15)
        tk.Label.__init__(self, parent, font=self.myFont, width=160, height=130, background="bisque")
        
        self.parent = parent
        self.backend = backend
        self.nextButton = nextButton
        
        
        self.backend.calculate_failrate()
        
        self.nextButton['state'] = tk.DISABLED

        self.label = tk.Label(self, text="There is 10 action points,\n Allocate points to features to decrease the failing rate",
        width=100, height=5, font=self.myFont,
         background="white")
        self.label.pack(anchor="w", padx=5, pady=5)

        self.featureList = []
        self.entryList = []
        self.vcmd = (self.register(self.callback))
        for i in range(len(self.backend.featureSelected)):
            self.featureList.append(tk.Label(self, text="feature name: " + self.backend.featureSelected[i].feature_name + "\n failing rate: {:3.0f}%".format(self.backend.featureSelected[i].fail_rate*100),
                width=80, height=3, font=self.myFont,
                background="white")) 
            self.entryList.append(tk.Entry(self, bd=2, width=20, validate='all', validatecommand=(self.vcmd, '%P')))

            self.featureList[i].pack(anchor="nw", padx=10, pady=5)
            self.entryList[i].pack(anchor="ne", padx=10, pady=5)
            self.entryList[i].insert(0,'0')


        self.confirmButton = tk.Button(self, text="Confirm Allocation",
                            width=20, height=2, font=self.myFont, bg="white",
                            command=self.confirm)
        self.confirmButton.pack(anchor="se", pady=10)

        

    def callback(self, P):
        if (str.isdigit(P) and int(P) <= 10) or P == "":
            return True
        else:
            return False

    def isTen(self):
        sum = 0
        for i in range(len(self.entryList)):
            if self.entryList[i].get() == "":
                continue
            if int(self.entryList[i].get()) < 0 or int(self.entryList[i].get()) > 10:
                return False

            sum += int(self.entryList[i].get())
        
        if sum <= 10:
            return True
        return False
    
    def confirm(self):
        if self.isTen():
            for i in range(len(self.entryList)):
                val = 0
                if self.entryList[i].get() != "":
                    val = int(self.entryList[i].get())
                self.backend.point_set(i, val)

                self.featureList[i].destroy()
                self.entryList[i].destroy()

            self.confirmButton.destroy()
            self.configure(text="All set! Please move on!")
            self.nextButton['state'] = tk.NORMAL
            #print([self.backend.featureSelected[i].points for i in range(len(self.entryList))])
