import socket
import pickle

class network:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = "10.216.20.212" # 192.168.10.64 10.216.20.212
		self.port = 5555
		self.addr = (self.server, self.port)
		self.player = self.connect()

	def getPlayer(self):
		return self.player

	def connect(self):
		try:
			self.client.connect(self.addr)
			return pickle.loads(self.client.recv(2048))

		except:
			pass

	def send(self, data):
		try:
			self.client.send(pickle.dumps(data))
			return pickle.loads(self.client.recv(2048))
		except socket.error as e:
			print(e)
