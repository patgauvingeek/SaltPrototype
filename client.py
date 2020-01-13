import common
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

# animation
animation = "|/-\\"
i = 0

try:
  # Send data
  while True:
    message = common.salted_hash(common.hash("1234"))
    encoded_message = message.encode()
    sock.sendall(len(encoded_message).to_bytes(4, byteorder="little"))
    sock.sendall(encoded_message)

    data = sock.recv(1).decode()
    if data == "F":
      print('FAILED !')
    else:
      # animation
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()
      i = i + 1
finally:
  print('closing socket')
  sock.close()
