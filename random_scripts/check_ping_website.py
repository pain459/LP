import os


def ping_check(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response:
        print("UP")
    else:
        print("DOWN")


ping_check("google.com")