from pythonosc.udp_client import UDPClient


class OscUdpClient:
    def __init__(self, ip, port, allow_broadcast=False):
        self._udp_client = UDPClient(ip, port, allow_broadcast)

    def send(self, content):
        self._udp_client.send(content)
