class OSCController:

    def __init__(self, client, interface):
        self.client, self.interface = client, interface
        self.interface.sender = self.client
        self.interface.loop()
