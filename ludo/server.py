import socket
from _thread import *
import sys
import pickle

server = "10.216.20.212" # IPV4 ADDR HERE 192.168.10.64 10.216.20.212
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port)) # 

except socket.error as e:
	str(e)

s.listen(4) #up to 6 connections 

print("Started server, Waiting for connection")

#store piece starting positions and changes
#pos = [[(,)(,)(,)(,)],[(,)(,)(,)(,)],[(,)(,)(,)(,)],[(,)(,)(,)(,)]]
#list of tuples

def threaded_client(conn, player):
	reply = ""
	conn.send(str.encode("Connected"))
	while True:
		try:
			data = pickle.loads(conn.recv(2048))
			pos[currentPlayer] = data
			if not data:
				print("Disconnected")
				break
			else:
				reply = pos
				print("Received: ", data)
				print("Sending: ", reply)
			conn.sendall(pickle.dumps(reply))
		except:
			break
	print("Lost connection")
	conn.close()

currentPlayer = 0
while True:
	conn, addr = s.accept()
	print("Connected to: ", addr)
	conn.send(pickle.dumps(currentPlayer))

	start_new_thread(threaded_client, (conn, currentPlayer))
	currentPlayer += 1
