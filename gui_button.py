from tkinter import *

root = Tk()

def checkclicked(event):
    print("Yes it was clicked")



button1 = Button(root, text="Click Here")
button1.bind("<Button-1>",checkclicked)
button1.pack()

root.mainloop()
