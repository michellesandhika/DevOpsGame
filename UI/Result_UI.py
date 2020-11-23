import tkinter as tk
import tkinter.font as font
from tkinter.messagebox import showinfo

class Result(tk.Label):
    def __init__(self, parent, backend):
        self.myFont = font.Font(size=15)
        tk.Label.__init__(self, parent, width=160, height=130, background="white")
        self.parent = parent
        self.backend = backend

        
        self.backend.add_total_metrics()
        self.backend.ending()


        self.feedback = self.backend.get_customer_feedback() # pop up
        showinfo(self.feedback)

        self.metrics = self.backend.get_total_metrics()
        self.result = tk.Label(self, text=
        '''
        Round {} result:\n\n
                Your Score is: {} \n
                \tlead time: {} \n
                \tfailed deployment: {}\n
                \tdeployment size: {} 
            
        '''.format( self.backend.round,
                    self.backend.score,
                    self.metrics.deploymentSize,
                    self.metrics.leadTime,
                    self.metrics.failedDeployment
                    ),
        width=70, height=30, font=self.myFont,
         background="white", justify=tk.LEFT, anchor="w")

        self.result.pack(anchor="n", padx=10, pady=5)

        self.backend.reset()
        