import ipaddress

class Ipv6:  #class for networking 531
    def convertusingipaddress(ipv4address):
        print(ipaddress.IPv6Address('2018::' + ipv4address).compressed) #print the result
    convertusingipaddress("10.10.10.10")  #from IPv4
    convertusingipaddress("150.100.250.200")
