class OSCController:

    def __init__(self, client, interface):
        self.client = client
        self.interface = interface

        self.interface.loop()
