# This is the template code for the CNE335 Final Project
#Matt Bennett
#CNE 335 3/7/2023
#Create a script to ping our EC2 instance


from Server import Server
def print_program_info():

    print("Server Automator v0.1 by Matt Bennett")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()

    pong = Server('52.41.145.87', 'C:\\Users\\mwben\\mattb_key.ppk')

    print(pong.ping())

    pong.update()
