import os

def process_command(user_input):
    # УЯЗВИМОСТЬ: Command Injection через os.system
    os.system("ping -c 1 " + user_input)
    return "Done"
