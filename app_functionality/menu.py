import subprocess
from app_functionality import vulScan, ipCheck, ufwSetup

def show_homepage():
    print("")
    print("          === Network Defender ===          ")
    print("------------------------------------------- ")
    print("| 1.    Vulnerability Scans     | 2.    Firewall Setup  |")
    print("-------------------------------------------  ")
    print("------------------------------------------")
    print("| 3.  Network Scans     | 4.    Intrusion Detection   |")
    print("------------------------------------------")
    print("              5. Exit                      |   ")


def menu_options():

    # uc stands for User Choice
    uc = int(input("Please choose a menu option: "))

    if uc == 1:
        vulScan.v_scans()
    elif uc == 2:
        ufwSetup.firewall_setup()

    if uc == 5:
        exit()
