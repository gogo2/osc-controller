import tkinter as tk

from osccontroller.helpers import osc_message
from osccontroller.option_containers import ButtonOptions, ScaleOptions


class GraphicalInterface:

    def __init__(self, width: int, height: int, client, title: str = "OSCController"):
        self.tk_root = tk.Tk()
        self.tk_root.title(title)
        self.tk_root.geometry('%dx%d' % (width, height))
        self.elements = []
        self.client = client

    def loop(self):
        self.tk_root.mainloop()

    def add_button(self, x: int, y: int, text: str, options: ButtonOptions = ButtonOptions(),
                   address=None, non_osc_content=None, osc_content=None, command=None):
        options_dict = {arg: val for arg, val in options._asdict().items() if val is not None}
        if address is not None:
            if non_osc_content is None:
                self.elements.append(tk.Button(self.tk_root, text=text, cnf=options_dict,
                                               command=lambda: self.client.send(osc_message(address))))
            else:
                self.elements.append(tk.Button(self.tk_root, text=text, cnf=options_dict,
                                               command=lambda: self.client.send(osc_message(address, non_osc_content))))
        elif osc_content is not None:
            self.elements.append(tk.Button(self.tk_root, text=text, cnf=options_dict,
                                           command=lambda: self.client.send(osc_content)))
        elif command is not None:
            self.elements.append(tk.Button(self.tk_root, text=text, command=command, cnf=options_dict))
        else:
            raise Exception()
        self.elements[-1].place(x=x, y=y)

    def add_scale(self, x: int, y: int, text: str, min_val, max_val, options: ScaleOptions = ScaleOptions(),
                  address: str = None, command=None):
        options_dict = {arg: val for arg, val in options._asdict().items() if val is not None}
        if address is not None:
            self.elements.append(tk.Scale(self.tk_root, text=text, from_=min_val, to=max_val, cnf=options_dict,
                                          command=lambda value: self.client.send(osc_message(address, [value]))))
        elif command is not None:
            self.elements.append(
                tk.Button(self.tk_root, text=text, from_=min_val, to=max_val, command=command, cnf=options_dict))
        else:
            raise Exception()
        self.elements[-1].place(x=x, y=y)
