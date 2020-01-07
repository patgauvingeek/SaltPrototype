import common
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
sock.settimeout(1.0)

# Wait for a connection
print('waiting for connections')
while True:
  try:
    connection, client_address = sock.accept()
    try:
      print('connection from', client_address)

      # Receive the data in small chunks and retransmit it
      while True:
        data = connection.recv(4)
        size = int.from_bytes(data, byteorder="little")
        data = connection.recv(size).decode()
        password_hash = common.salted_hash("1234")
        if data == password_hash:
          connection.sendall("T".encode())
        else:
          print(data)
          print(password_hash)
          connection.sendall("F".encode())
    except ConnectionAbortedError as e:
      pass
    finally:
      # Clean up the connection
      connection.close()
  except socket.timeout as e:
    pass