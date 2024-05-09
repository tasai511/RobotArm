from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

### Global valuable ###
def_run_status = True
def_servo0_close = 30
def_servo0_open = 130
def_servo1_low = 125
def_servo1_high = 90
def_servo2_catch = 0
def_servo2_drop = 150
def_servo3_open = 0
def_servo3_close = 100
def_counter = 0
def_step = 0
def_delay = 1500
def_speed = 3

v_coils  = {0:def_run_status}
v_i_regs = {0:def_counter, 1:def_step}
v_h_regs = {\
  50:def_servo0_close, 51:def_servo0_open, \
  52:def_servo1_low,   53:def_servo1_high, \
  54:def_servo2_catch, 55:def_servo2_drop, \
  56:def_servo3_open,  57:def_servo3_close,\
  58:def_delay,        59:def_speed        \
}


### Functions ###
class MyDataBank(DataBank):
  global v_coils
  global v_i_regs
  global v_h_regs
  
  def __init__(self):
    super().__init__(virtual_mode=True)

  def get_coils(self, address, number=1, srv_info=None):
    try:
      return [v_coils[a] for a in range(address, address+number)]
    except KeyError:
      return
      
  def get_holding_registers(self, address, number=1, srv_info=None):
    try:
      return [v_h_regs[a] for a in range(address, address+number)]
    except KeyError:
      return

  def get_input_registers(self, address, number=1, srv_info=None):
    try:
      return [v_i_regs[a] for a in range(address, address+number)]
    except KeyError:
      return
      
  def set_coils(self, address, bit_list, srv_info=None):
    bit_list = [bool(b) for b in bit_list]
    if (address >= 0) and (address + len(bit_list) <= len(v_coils)):
      for a in range(address, address + len(bit_list)):
        v_coils[a] = bit_list[a-address]
      return True   
    else:
      return None

  def set_holding_registers(self, address, word_list, srv_info=None):
    word_list = [int(w) & 0xffff for w in word_list]
    if (address >= 50) and (address + len(word_list) <= 50 + len(v_h_regs)):
      for a in range(address, address + len(word_list)):
        v_h_regs[a] = word_list[a-address]
      return True   
    else:
      return None


### Initialize ###
server = ModbusServer("10.45.0.4", 502, no_block=True, data_bank=MyDataBank())
print("Start Modbus Server...")
server.start()
print("Modbus Server is Online")
print("Start Robot...")
print("Robot is Online")


### Main Loop ###
while True:
  run_status   =  v_coils[0]
  servo0_close = v_h_regs[50]
  servo0_open  = v_h_regs[51]
  servo1_low   = v_h_regs[52]
  servo1_high  = v_h_regs[53]
  servo2_catch = v_h_regs[54]
  servo2_drop  = v_h_regs[55]
  servo3_open  = v_h_regs[56]
  servo3_close = v_h_regs[57]
  delay        = v_h_regs[58]

  if run_status == True:
    v_i_regs[1] = 0

    sleep(delay/1000)
    v_i_regs[1] = 1 #step

    sleep(delay/1000)
    v_i_regs[1] = 2 #step

    sleep(delay/1000)
    v_i_regs[1] = 3 #step

    sleep(delay/1000)   
    v_i_regs[1] = 4 #step

    v_i_regs[0] = v_i_regs[0] + 1 #counter