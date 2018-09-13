from osccontroller.graphical_interface import GraphicalInterface
from osccontroller.option_containers import ButtonOptions, ScaleOptions


class SimpleGraphicalInterface:

    def __init__(self, width: int, height: int, client, start_maximized=False, title: str = "OSCController"):
        self.root = GraphicalInterface(width, height, client, start_maximized, title)
        self.elements = []

    def loop(self):
        self.root.loop()

    def add_button(self, x: int, y: int, text: str, options: ButtonOptions = ButtonOptions(),
                   address=None, non_osc_content=None, osc_content=None, command=None):
        self.elements.append(self.root.make_button(text, options, address, non_osc_content, osc_content, command))
        self.elements[-1].place(x=x, y=y)
        return self.elements[-1]

    def add_scale(self, x: int, y: int, label: str, init_val, min_val, max_val, options: ScaleOptions = ScaleOptions(),
                  address: str = None, command=None):
        self.elements.append(self.root.make_scale(label, init_val, min_val, max_val, options, address, command))
        self.elements[-1].place(x=x, y=y)
        return self.elements[-1]
