import tkinter as tk
import tkinter.font as font

class Production(tk.Label):
    def __init__(self, parent, backend):
        self.myFont = font.Font(size=15)
        tk.Label.__init__(self, parent, width=160, height=130, background="white", text="Production")
        self.parent = parent
        self.backend = backend

        self.backend.deploy()
        self.metrics = self.backend.return_current_metrics()
        self.failures = ["\n\t\t" + f.feature_name for f in self.backend.return_failed_features()]
        self.failures = "".join(self.failures)

        self.result = tk.Label(self, text=
        '''
        Results:\n\n
            Affected Metrics:
                \n\t\tleadtime: {}
                \n\t\tfailed deployment: {}
                \n\t\tdeployment size: {} \n\n
            Deployment failure:
                {}
        '''.format( self.metrics.leadTime,
                    self.metrics.failedDeployment,
                    self.metrics.deploymentSize,
                    self.failures
                    ),
        width=50, height=30, font=self.myFont,
         background="white", justify=tk.LEFT, anchor="w")



        self.result.pack(anchor="n", padx=10, pady=5)
