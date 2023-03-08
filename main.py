# This is the template code for the CNE335 Final Project
#Matt Bennett
#CNE 335 3/7/2023
#Create a script to ping our EC2 instance


from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Matt Bennett")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    pong = Server("52.41.145.87")
    # TODO - Call Ping method and print the results
    print(pong.ping())
