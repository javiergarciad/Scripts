
#!python



def check_reboot():
    """Returns True if a reboot is pending on a Linux machine
    """
    return os.path.exist("/run/reboot-required")

    
def main():
    print("Hello!")

main()
