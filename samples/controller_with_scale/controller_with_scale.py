from osccontroller.graphical_inrerface import GraphicalInterface
from osccontroller.option_containers import ScaleOptions
from osccontroller.osc_client import OscUdpClient

CURR = 0
LAST = 10


def main():
    client = OscUdpClient("10.0.0.188", 8000)
    interface = GraphicalInterface(350, 350, client, "scale")

    interface.add_scale(50, 50, "Brightness", 0.5, 0., 1.,
                        ScaleOptions(background="#55AA55", foreground="#ffffff", font=('halvetica', 12),
                                     resolution=-1, length=200, orient="horizontal"),
                        address="/surfaces/Quad/Brightness")

    interface.loop()
