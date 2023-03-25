import subprocess
import ipCheck
import menu

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
            ip = ipCheck.ip_check()
            subprocess.run(["nmap", "-A", ip])
            
        elif uc == 2:
            ip = ipCheck.ip_check()
            subprocess.run(["nmap", "-Pn", ip])

        elif uc == 3:
            ip = ipCheck.ip_check()
            subprocess.run(["nmap" , "-O", ip])

        elif uc == 4:
            ip = ipCheck.ip_check()
            subprocess.run(["nmap", "-sV", ip])

        elif uc == 5:
            menu.show_homepage()
            menu.menu_options()

        else:
            print("Please make a valid choice")

