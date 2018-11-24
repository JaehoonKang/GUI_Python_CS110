from tkinter import *

root = Tk() #root => window

root.title("The first GUI")
#root.iconbitmap(r'c:\sys.ico') => create an icon
#myLabel = Label(root, text="I love myself")
#myLabel.pack()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="button1", fg="red")
button2 = Button(topFrame, text="button1", fg="blue")
button3 = Button(topFrame, text="button1", fg="green")
button4 = Button(topFrame, text="button1", fg="purple")

button1.pack()
button2.pack()
button3.pack()
button4.pack()


root.mainloop() #make sure the window shows up and not disappear
