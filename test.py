from pylibmodbus import ModbusRtu


#Define Modbus RTU client (Python 2.x)
client=ModbusRtu(device="/dev/serial0", baud=19200, parity="N", data_bit=8, stop_bit=1)
# For Python 3.x you have to explicitly indicate ASCII enconding
#client=ModbusRtu(device="/dev/serial0".encode("ascii"), baud=19200, parity="N".encode("ascii"), data_bit=8, stop_bit=1)

#Read and set timeout
timeout_sec = client.get_response_timeout()
client.set_response_timeout(timeout_sec+1)

#Connect
client.connect()

SERVER_ID=0
BCM_PIN_DE=17
BCM_PIN_RE=9

#Set Slave ID number
client.set_slave(SERVER_ID)

#Enable RPi GPIO Functions
client.enable_rpi(1)

#Define pin numbers to be used as Read Enable (RE) and Drive Enable (DE)
client.configure_rpi_bcm_pins(BCM_PIN_DE,BCM_PIN_RE)

#Export pin direction (set as outputs)
client.rpi_pin_export_direction()

#Write Modbus registers, 10 starting from 0
client.write_registers(0, [0]*10)

#Read 10 input registers starting from number 0
result=(client.read_registers(0, 10))

#Show register values
print result

#Release pins and close connection
client.rpi_pin_unexport_direction()
client.close()
