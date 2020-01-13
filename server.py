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

# animation
animation = "|/-\\"
i = 0

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
        if data == "":
          sys.stdout.write("\rClient Gone\n")
          break
        
        password_hashes = common.accepted_salted_hashes(common.hash("1234"))
          
        if data in password_hashes:
          connection.sendall("T".encode())
          # animation
          sys.stdout.write("\r" + animation[i % len(animation)])
          sys.stdout.flush()
          i = i + 1
        else:
          print(data)
          print(password_hashes)
          connection.sendall("F".encode())
    except ConnectionAbortedError as e:
      pass
    finally:
      # Clean up the connection
      connection.close()
  except socket.timeout as e:
    pass