import subprocess
from app_functionality import menu


def start_tshark(interface, output_file=None, capture_filter=None):
    # Start tshark with the specified interface, output file, and capture filter
    command = ["tshark", "-i", interface]
    if output_file:
        command.extend(["-w", output_file])
    if capture_filter:
        command.extend(["-f", capture_filter])
    process = subprocess.Popen(command)
    return process

def stop_tshark(process):
    # Stop tshark process
    process.kill()

def capture_packets(interface, output_file=None, capture_filter=None):
    # Capture packets on the specified interface, apply capture filter, and save to output file if provided
    process = start_tshark(interface, output_file, capture_filter)
    print("Capturing packets on interface", interface, "...")
    input("Press enter to stop capturing...")
    stop_tshark(process)
    print("Packet capture stopped.")
    return output_file

def display_interfaces():
    # Display available interfaces
    print("Available interfaces:")
    result = subprocess.run(["tshark", "-D"], stdout=subprocess.PIPE)
    interfaces = result.stdout.decode().splitlines()
    for i, interface in enumerate(interfaces):
        print(f"{i+1}. {interface}")
    return interfaces

def display_menu():
    # Display capture options menu and capture user input
    print("                  === Network Capture ===          ")
    print("                === Tshark Capture Menu ===        ")
    print("        ------------------------------------------- ")
    print("| 1.    Capture on all available interfaces   | 2.    Choose an interface to capture on    |")
    print("        -------------------------------------------  ")
    print("         ------------------------------------------")
    print("| 3.  Apply a Capture Filter    | 4.    Save Capture to a File   |")
    print("             ------------------------------------------")
    print("                             5. Exit                      |   ")
    choice = input("Enter your choice: ")
    return choice

def start_capture():
    # Display capture options menu and capture user input
    choice = display_menu()
    output_file = None
    capture_filter = None
    interfaces = None

    # Process user input
    while choice != "5":
        if choice == "1":
            capture_packets(interfaces, output_file, capture_filter)
        elif choice == "2":
            interfaces = display_interfaces()
            interface_choice = input("Enter interface number: ")
            if interface_choice.isdigit() and 1 <= int(interface_choice) <= len(interfaces):
                interface = interfaces[int(interface_choice)-1]
                capture_packets(interface, output_file, capture_filter)
            else:
                print("Invalid interface number.")
        elif choice == "3":
            capture_filter = input("Enter capture filter: ")
            capture_packets(interfaces, output_file, capture_filter)
        elif choice == "4":
            output_file = input("Enter output file name: ")
            capture_packets(interfaces, output_file, capture_filter)
        else:
            print("Invalid choice.")
        choice = display_menu()
    menu.show_homepage()
    menu.menu_options()
