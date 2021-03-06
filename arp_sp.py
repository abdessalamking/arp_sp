import scapy.all as scapy
import argparse

def get_arguments():
     parser = argparse.ArgumentParser()
     parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range .")
     options = parser.parse_args()
     if not options.target:
        parser.error("[-] Please specify an Target , use --help for more info.")
     return options

def scan(ip):
     arp_request = scapy.ARP(pdst = ip )
     broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
     arp_request_broadcast = broadcast/arp_request
     answered_list= scapy.srp(arp_request_broadcast , timeout=1 )[0]
     clinet_list =[]
     for element in answered_list :
          clinet_dict = {"ip":element[1].psrc,"mac":element[1].hwdst}
          clinet_list.append(clinet_dict)
          return clinet_list
def print_result(client_result):
     print ("IP\t\t\tMAC address\n----------------------------------------------------")
     for client in client_result :
          print (client["ip"] + "\t\t" + client["mac"])

print("\t\t[++] Creat By Abdessalam King [++]\n")
options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
