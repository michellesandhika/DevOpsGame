from tkinter import *

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("900x600")
root.config(bg="green")


#create containers
top_frame = Frame(root, bg="cyan", width =900, height = 100)
top_frame.pack()

bottom_frame = Frame(root, bg="red", width=900, height = 500)
bottom_frame.pack(side=BOTTOM)

testLabel = Label(top_frame, text="This is a test label")
testLabel.pack(side=TOP)

root.mainloop()