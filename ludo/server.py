import time
import socket
from _thread import *
import sys
import pickle
import player

server = "10.216.27.161" # IPV4 ADDR HERE 192.168.10.64 10.216.20.212 10.216.27.161
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port)) # 

except socket.error as e:
	str(e)

s.listen(4) #up to 6 connections 

print("Started server, Waiting for connection")

currentPlayer = 0

mover = 0

clients = []


def threaded_client(conn, curr):
	data = []
	conn.send(pickle.dumps(curr))
	while True:
		reply = [[], [], [], []]
		time.sleep(2)
		reply[curr] = []
		data = pickle.loads(conn.recv(16000))
		reply[curr] = data
		global mover
		if not isinstance(data, int):
			print(reply)
			for cli in clients:
				cli.send(pickle.dumps(reply))
			if mover == 3:
				mover = 0
			else:
				mover = curr + 1
		if mover == curr:
			print("br")
			conn.send(pickle.dumps("br"))
	print("Lost connection")
	conn.close()

while True:
	conn, addr = s.accept()
	print("Connected to: ", addr)
	clients.append(conn)
	start_new_thread(threaded_client, (conn, currentPlayer))
	currentPlayer += 1