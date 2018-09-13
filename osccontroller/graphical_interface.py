import tkinter as tk

from osccontroller.helpers import osc_message, num_val
from osccontroller.option_containers import ButtonOptions, ScaleOptions


class GraphicalInterface:

    def __init__(self, width: int, height: int, client, start_maximized=False, title: str = ""):
        self.tk_root = tk.Tk()
        self.tk_root.title(title)
        self.tk_root.geometry('%dx%d' % (width, height))
        if start_maximized:
            self.tk_root.state("zoomed")
        self.client = client

    def loop(self):
        self.tk_root.mainloop()

    def make_button(self, text: str, options: ButtonOptions = ButtonOptions(),
                    address=None, non_osc_content=None, osc_content=None, command=None):
        options_dict = {arg: val for arg, val in options._asdict().items() if val is not None}
        if address is not None:
            if non_osc_content is None:
                button = tk.Button(self.tk_root, text=text, cnf=options_dict,
                                   command=lambda: self.client.send(osc_message(address)))
            else:
                button = tk.Button(self.tk_root, text=text, cnf=options_dict,
                                   command=lambda: self.client.send(osc_message(address, non_osc_content)))
        elif osc_content is not None:
            button = tk.Button(self.tk_root, text=text, cnf=options_dict,
                               command=lambda: self.client.send(osc_content))
        elif command is not None:
            button = tk.Button(self.tk_root, text=text, command=command, cnf=options_dict)
        else:
            raise Exception()
        return button

    def make_scale(self, label: str, init_val, min_val, max_val, options: ScaleOptions = ScaleOptions(),
                   address: str = None, command=None):
        options_dict = {arg: val for arg, val in options._asdict().items() if val is not None}
        if address is not None:
            scale = tk.Scale(self.tk_root, label=label, from_=min_val, to=max_val, cnf=options_dict,
                             command=lambda val: self.client.send(osc_message(address, [num_val(val)])))
        elif command is not None:
            scale = tk.Button(self.tk_root, label=label, from_=min_val, to=max_val, command=command, cnf=options_dict)
        else:
            raise Exception()
        scale.set(init_val)
        return scale
