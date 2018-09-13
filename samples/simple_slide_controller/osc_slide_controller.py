from osccontroller.helpers import osc_message, osc_bundle
from osccontroller.option_containers import ButtonOptions
from osccontroller.osc_client import OscUdpClient
from osccontroller.simple_graphical_inrerface import SimpleGraphicalInterface

CURR = 0
LAST = 10


def main():
    client = OscUdpClient("10.0.0.188", 8000)
    interface = SimpleGraphicalInterface(640, 300, client, "3D meetup #7")
    select_msg = osc_message("/Prez")

    def prev_slide():
        global CURR
        if CURR > 0:
            CURR -= 1
            bundle = osc_bundle([select_msg, osc_message('/Slide' + str(CURR))])
            client.send(bundle)

    def next_slide():
        global CURR
        if CURR < LAST:
            CURR += 1
            bundle = osc_bundle([select_msg, osc_message('/Slide' + str(CURR))])
            client.send(bundle)

    interface.add_button(50, 50, "PREV",
                         ButtonOptions(background="#5555ff", foreground="#ffffff", font=('halvetica', 52)),
                         command=prev_slide)

    interface.add_button(350, 50, "NEXT",
                         ButtonOptions(background="#55AA55", foreground="#ffffff", font=('halvetica', 52)),
                         command=next_slide)

    interface.loop()
