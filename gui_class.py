from tkinter import *

class Learning:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(master, text="Printing Message", command = self.printMessage)
        self.quitButton = Button(master, text="Quit", command = master.quit)

        self.printButton.pack(side=LEFT)
        self.quittButton.pack(side=LEFT)

    def printMessage(self):
        print("This works pretty well")


root = Tk()
Learning(root)
root.mainloop()
