import tkinter as tk


class GraphicalInterface:

    def __init__(self, width, height, title="OSCController"):
        self.tk_root = tk.Tk()
        self.tk_root.title(title)
        self.tk_root.geometry("%dX%d" % (width, height))

    def loop(self):
        self.tk_root.mainloop()

    def add_button(self):
        pass
