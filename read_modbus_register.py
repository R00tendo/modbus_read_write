from pymodbus.client.sync import ModbusTcpClient
import sys


if len(sys.argv) <= 3:
   print("Usage: python3 script.py   ip   start_register end_register")
   sys.exit(0)


client = ModbusTcpClient(sys.argv[1], port=502)
client.connect()
req = client.read_holding_registers(int(sys.argv[2]), int(sys.argv[3]))
print(req.registers)
