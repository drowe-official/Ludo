import socket
from _thread import *
import sys

server = "10.216.20.212" # IPV4 ADDR HERE
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

def read_pos(str):
	str = str.split(",")
	return int(str[0]), int(str[1]), int(str[2]), int(str[3])

def make_pos(tup):
	return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3])

def threaded_client(conn, player):
	reply = ""
	conn.send(str.encode("Connected"))
	conn.send(str.encode(make_pos(pos[player])))
	while True:
		try:
			data = read_pos(conn.recv(2048).decode())
			pos[currentPlayer] = data
			if not data:
				print("Disconnected")
				break
			else:
				reply = pos
				print("Received: ", data)
				print("Sending: ", reply)
			conn.sendall(str.encode(make_pos(reply)))
		except:
			break
	print("Lost connection")
	conn.close()

currentPlayer = 0
while True:
	conn, addr = s.accept()
	print("Connected to: ", addr)

	start_new_thread(threaded_client, (conn, currentPlayer))
	currentPlayer += 1
