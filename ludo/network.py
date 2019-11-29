import socket
import pickle

class network:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = "10.216.27.161" # 192.168.10.64 10.216.20.212 10.216.27.161
		self.port = 5555
		self.addr = (self.server, self.port)
		self.bo = self.connect()

	def getBo(self):
		self.Bo = self.connect()
		return self.bo

	def connect(self):
		try:
			self.client.connect(self.addr)
			return pickle.loads(self.client.recv(160000))
		except:
			pass

	def send(self, data):
		try:
			self.client.send(pickle.dumps(data))
			return pickle.loads(self.client.recv(160000))
		except socket.error as e:
			print(e)
