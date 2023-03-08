import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        # Adapted from https://www.delftstack.com/howto/python/python-ping/
        os.system("ping -n 5 " + self.server_ip)
        return "Nice job pinging, bruh!"
