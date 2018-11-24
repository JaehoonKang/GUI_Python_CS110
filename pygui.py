from tkinter import *

root = Tk() #root => window

root.title("The first GUI")
#root.iconbitmap(r'c:\sys.ico') => create an icon
myLabel = Label(root, text="I love myself")
myLabel.pack()
root.mainloop() #make sure the window shows up and not disappear
