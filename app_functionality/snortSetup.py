import subprocess
from app_functionality import menu


def configure_snort_rules():
    while True:
        print("")
        print("                     === IDS Setup ===          ")
        print("          === Snort Rule Configuration Menu === ")
        print("             ------------------------------------------- ")
        print("| 1.    Enable/Disable a Rule       | 2.    Add a New Rule  |")
        print("         -------------------------------------------  ")
        print("         ------------------------------------------")
        print("| 3.  Delete an Existing Rule    | 4.    View Current Rules   |")
        print("             ------------------------------------------")
        print("                             5. Exit                      |   ")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            enable_disable_rule()
        elif choice == '2':
            add_new_rule()
        elif choice == '3':
            delete_existing_rule()
        elif choice == '4':
            view_current_rules()
        elif choice == '5':
            print("Exiting Snort Rule Configuration Menu...")
            menu.show_homepage()
            menu.menu_options()
            break
        else:
            print("Invalid choice. Please try again.")

def enable_disable_rule():
    rule_id = input("Enter the ID of the rule you want to enable/disable: ")
    enable = input("Do you want to enable or disable the rule? (enable/disable): ")

    # Execute the Snort command-line interface to enable/disable the rule
    subprocess.run(["sudo", "snort", "-Tc", "/etc/snort/snort.conf"])
    subprocess.run(["sudo", "snort", "-R", rule_id, enable])

def add_new_rule():
    # Prompt the user to enter the rule details
    rule_type = input("Enter the rule type (e.g. alert, log): ")
    rule_protocol = input("Enter the rule protocol (e.g. TCP, UDP): ")
    rule_source = input("Enter the rule source (e.g. any, !192.168.1.1): ")
    rule_destination = input("Enter the rule destination (e.g. any, 192.168.1.1): ")
    rule_port = input("Enter the rule port (e.g. 80, 443): ")
    rule_action = input("Enter the rule action (e.g. drop, pass): ")

    # Construct the Snort rule string
    rule = f"{rule_type} {rule_protocol} {rule_source} {rule_port} -> {rule_destination} {rule_port} ({rule_action})"

    # Execute the Snort command-line interface to add the new rule
    subprocess.run(["sudo", "snort", "-Tc", "/etc/snort/snort.conf"])
    subprocess.run(["sudo", "snort", "-R", "-q", rule])

def delete_existing_rule():
    rule_id = input("Enter the ID of the rule you want to delete: ")

    # Execute the Snort command-line interface to delete the rule
    subprocess.run(["sudo", "snort", "-Tc", "/etc/snort/snort.conf"])
    subprocess.run(["sudo", "snort", "-R", "-q", "-D", rule_id])

def view_current_rules():
    # Execute the Snort command-line interface to view the current rules
    output = subprocess.run(["sudo", "snort", "-Tc", "/etc/snort/snort.conf", "-c",
                             "echo 'output alert_csv: stdout' >> /etc/snort/snort.conf && snort -c /etc/snort/snort.conf -N -A alert_csv -q"],
                            capture_output=True, text=True)
    print(output.stdout)
