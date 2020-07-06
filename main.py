"""
client = ModbusTcpClient(host='192.168.1.50',port=502)
client.connect()


#bus = client.read_input_registers(0x2030, 65)

client.write_coil(0,False)
client.read_coils(0,4)
"""
import fonction
from pymodbus.client.sync import ModbusTcpClient
client = ModbusTcpClient(host='192.168.1.102',port=502)
client.connect()
client.write_coil(0,True)
fonction.lireEntree(client,1)
print(fonction.lireEntree(client,1))