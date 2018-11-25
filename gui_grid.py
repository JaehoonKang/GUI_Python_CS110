from tkinter import *

root = Tk()

def checkState():
    #print(var.get())
    if var.get() == 1:
        print("Checkbox is changed")
    else:
        print("Not changed")

label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky = E)
label_2.grid(row=1, column=0, sticky = E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

var = IntVar() #tkinter variable to save a value

c = Checkbutton(root, text = "Keep me logged in", command = checkState, variable = var)
c.grid(columnspan = 2)



root.mainloop()
