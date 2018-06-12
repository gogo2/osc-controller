import tkinter as tk

from osccontroller.option_containers import ButtonOptions


class GraphicalInterface:

    def __init__(self, width: int, height: int, client, title: str = "OSCController"):
        self.tk_root = tk.Tk()
        self.tk_root.title(title)
        self.tk_root.geometry('%dx%d' % (width, height))
        self.elements = []
        self.client = client

    def loop(self):
        self.tk_root.mainloop()

    def add_button(self, x: int, y: int, text: str, options: ButtonOptions = ButtonOptions(), osc_content=None,
                   command=None):
        options_dict = {}
        for arg, val in options._asdict().items():
            if val is not None:
                options_dict[arg] = val
        if osc_content is not None:
            self.elements.append(tk.Button(self.tk_root,
                                           text=text,
                                           command=lambda content=osc_content: self.client.send(content),
                                           cnf=options_dict))
        elif command is not None:
            self.elements.append(tk.Button(self.tk_root, text=options.text, command=command, cnf=options_dict))
        else:
            raise Exception()
        self.elements[-1].place(x=x, y=y)
