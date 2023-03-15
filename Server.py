import os
import paramiko


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, keypath):
        # TODO -
        self.server_ip = server_ip
        self.keypath = keypath

    def ping(self):
        # TODO - Use os module to ping the server
        # Adapted from https://www.delftstack.com/howto/python/python-ping/
        os.system("ping -n 5 " + self.server_ip)
        return "Nice job pinging, bruh!"

    def update(self):
        #https://blog.ruanbekker.com/blog/2018/04/23/using-paramiko-module-in-python-to-execute-remote-bash-commands/
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname = f'{self.server_ip}', username = 'ubuntu', key_filename = self.keypath )

        stdin, stdout, stderr = ssh.exec_command('lsb_release -a')

        for line in stdout.read().splitlines():
            print("\b")
            print(line)

        #https://embeddedinventor.com/sudo-apt-get-update-y-command-explained-for-beginners/
        stdin, stdout, stderr = ssh.exec_command('sudo apt-get update && sudo apt-get -y upgrade')

        for line in stdout.read().splitlines():
            print("\b")
            print(line)

        ssh.close()

