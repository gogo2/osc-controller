import tkinter as tk

from osccontroller.option_containers import ButtonOptions
from osccontroller.osc_client import OSCClient


class GraphicalInterface:

    def __init__(self, width: int, height: int, client: OSCClient, title: str = "OSCController"):
        self.tk_root = tk.Tk()
        self.tk_root.title(title)
        self.tk_root.geometry("%dX%d" % (width, height))
        self.elements = []
        self.client = client

    def loop(self):
        self.tk_root.mainloop()

    def add_button(self, options: ButtonOptions):
        if options.osc_content is not None:
            self.elements.append(tk.Button(self.tk_root,
                                           text=options.text,
                                           command=lambda content=options.osc_content: self.client.send(content)))
        elif options.command is not None:
            self.elements.append(tk.Button(self.tk_root, text=options.text, command=options.command))
        self.elements[-1].pack()
