import subprocess
from app_functionality import ipCheck, menu



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
            ip = ipCheck.ip_check()
            subprocess.run(["sudo", "ufw", "deny", "from", ip])
        
        
        elif uc == 2:
            ip = ipCheck.ip_check()
            subprocess.run([f"sudo ufw allow from {ip}"])

        elif uc == 3:
            ip = ipCheck.ip_check()
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
            menu.show_homepage()
            menu.menu_options()