from tkinter import *


root = Tk()

photo = PhotoImage(file"angry.jpg")
label = Label(root, image = photo)
label.pack()


root.mainloop()
