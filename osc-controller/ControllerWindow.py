import tkinter as tk


class ControllerWindow:

    def __init__(self, width, height, title="OSCController"):
        tk_root = tk.Tk()
        tk_root.title(title)
        tk_root.geometry("%dX%d" % (width, height))

        tk_root.mainloop()
