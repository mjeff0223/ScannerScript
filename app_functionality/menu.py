import subprocess
import re


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


def ip_check():
    while True:

        ip = input("Enter target IPV4 address: ")

        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        p = re.compile(regex)

        if (re.search(p, ip)):
            print("valid ipv4")
            return True, ip
        else:
            return False


def v_scans():
    while True:

        print("")
        print("          === Vulnerability Scan ===          ")
        print("------------------------------------------- ")
        print("| 1.    Get all information     | 2.    Just Port info  |")
        print("-------------------------------------------  ")
        print("------------------------------------------")
        print("| 3.  Just operating system     | 4.    Services   |")
        print("------------------------------------------")
        print("              5. Exit                      |   ")

        uc = int(input("Please choose a menu option: "))
        if uc == 1:
            ip = ip_check()
            subprocess.run([f"nmap {ip} -A"])
            return
        elif uc == 2:
            if ip:
                same_ip = input("Is this the same target? Y or N: ")
                if same_ip == "y" or same_ip == "Y":
                    subprocess.run([f"nmap {ip} -Pn"])
                if same_ip == "N" or same_ip == "n":
                    ip = ip_check()
                    subprocess.run([f"nmap {ip} -Pn"])
        elif uc == 3:
            if ip:
                same_ip = input("Is this the same target? Y or N: ")
                if same_ip == "y" or same_ip == "Y":
                    subprocess.run([f"nmap {ip} -O"])
                if same_ip == "N" or same_ip == "n":
                    ip = ip_check()
                    subprocess.run([f"nmap {ip} -O"])
        elif uc == 4:
            if ip:
                same_ip = input("Is this the same target? Y or N: ")
                if same_ip == "y" or same_ip == "Y":
                    subprocess.run([f"nmap {ip} -sV"])
                if same_ip == "N" or same_ip == "n":
                    ip = ip_check()
                    subprocess.run([f"nmap {ip} -sv"])
        elif uc == 5:
            show_homepage()
            menu_options()

        else:
            print("Please make a valid choice")


def menu_options():

    # uc stands for User Choice
    uc = int(input("Please choose a menu option: "))

    if uc == 1:
        v_scans()

    if uc == 5:
        exit()
