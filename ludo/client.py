import socket


class Client:
    
    
    def __init__(self):
        self.socket = None
        
    def connect(self, ip, port): # connect to ip on port
        server_addr = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(server_addr)
        self.send("client joining")
        self.socket.recv(1024)
        #self.socket.setblocking(0)
    
    def disconnect(self): # disconnect socket from server
        self.socket.close()
        
    def send(self, msg): # send message to server
        print (msg, "being sent")
        self.socket.sendall(msg.encode("utf-8"))
        print("sent", msg, "to server")
    
    def receive(self): #receive message from server as string
        msg = self.socket.recv(1024)
        print ("received", msg.decode("utf-8"))
        return msg.decode("utf-8")
        
        
if __name__ == "__main__":
    server_ip = "127.0.0.1"
    server_port = 65432
    client = Client()
    client.connect(server_ip, server_port)
    while True:
        message = client.receive() # receive message from server
        if message:
            print (message, "received from server")