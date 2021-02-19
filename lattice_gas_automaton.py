from tkinter import *

class fluid_sim:
    def __init__(self):
        root = Tk()
        root.title("fluid simulation")

        canvas = Canvas(root, width=250, height=250)
        canvas.pack()

        root.mainloop()