import re


def ip_check():
    while True:

        ip_or_ip_sub = input("Is this an IPV4 address (I) or subnet CIDR range (S)?: I or S: ")
        if ip_or_ip_sub == "I" or ip_or_ip_sub == "i":
            ip = input("Enter target IPV4 address: ")

            regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
            p = re.compile(regex)

            if (re.search(p, ip)):
                print("valid ipv4")
                return ip
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