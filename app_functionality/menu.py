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

        ip_or_ip_sub = input("Is this an IPV4 address (I) or subnet CIDR range (S)?: I or S: ")
        if ip_or_ip_sub == "I" or ip_or_ip_sub == "i":
            ip = input("Enter target IPV4 address: ")

            regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
            p = re.compile(regex)

            if (re.search(p, ip)):
                print("valid ipv4")
                return True, ip
            else:
                print("Please input a valid IPV4 address")
                continue

        if ip_or_ip_sub == "S" or ip_or_ip_sub == "s":
            ip = input("Enter subnet CIDR range: ")

            regex_2 = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(\/[0-9][0-9])?$"
            a = re.compile(regex_2)

            if (re.search(a, ip)):
                print("valid ipv4 cidr")
                return True, ip
            else:
                print("Please input a valid IPV4 subnet cidr range")
                continue


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

def firewall_setup():
    while True:
        print("")
        print("                     === Firewall Setup ===          ")
        print("             ------------------------------------------- ")
        print("| 1.    Deny an IPV4 address                | 2.    Allow an IPV4 address  |")
        print("         -------------------------------------------  ")
        print("         ------------------------------------------")
        print("| 3.  Allow an SSH connection from IPV4    | 4.    Web Server options   |")
        print("             ------------------------------------------")
        print("                             5. Exit                      |   ")

        uc = int(input("Please choose a menu option: "))

        if uc == 1:
            ip = ip_check()
            subprocess.run([f"sudo ufw deny from {ip}"])
        
        
        elif uc == 2:
            ip = ip_check()
            subprocess.run([f"sudo ufw allow from {ip}"])

        elif uc == 3:
            ip = ip_check()
            subprocess.run([f"sudo ufw allow from {ip} proto tcp to any port 22"])
        
        elif uc == 4:
            web_server = input("What webserver are you using? N for Nginx A for Apache: ")

            if web_server == "N" or web_server == "n":
                protocol = input("What protocol do you want to allow: H for HTTP S for HTTPS: ")
                if protocol == "H" or protocol == "h":
                    subprocess.run(["sudo ufw allow \"Nginx HTTP\""])
                elif protocol == "S" or protocol == "S":
                    subprocess.run(["sudo ufw allow \"Nginx HTTPS\""])

            elif web_server == "A" or web_server == "a":
                protocol = input("What protocol do you want to allow: H for HTTP S for HTTPS: ")
                if protocol == "H" or protocol == "h":
                    subprocess.run(["sudo ufw allow \"Apache HTTP\""])
                elif protocol == "S" or protocol == "S":
                    subprocess.run(["sudo ufw allow \"Apache HTTPS\""])
        elif uc == 5:
            show_homepage()
            menu_options()



def menu_options():

    # uc stands for User Choice
    uc = int(input("Please choose a menu option: "))

    if uc == 1:
        v_scans()
    elif uc == 2:
        firewall_setup()

    if uc == 5:
        exit()
