from tkinter import *

root = Tk()

one = Label(root, text = "One",fg="white",bg="black")
one.pack()

two = Label(root, text = "Two",fg="black",bg="yellow")
two.pack(fill=BOTH, expand=TRUE)


three = Label(root, text = "Three",fg="green",bg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()
