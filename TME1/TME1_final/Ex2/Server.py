from socket import *
from threading import *
import time
from datetime import datetime


serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM) # Creating the socket and binding it to the port
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server ready')

def handle_client():
    while True:
        received = connectionSocket.recv(2048).decode('utf-8') # receiving from client
        if not received:
            connectionSocket.close() # Closing the socket if nothing is received from the client
            break
        else:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            to_send = datetime.strptime(current_time,"%H:%M:%S").encode('utf-8')
            connectionSocket.sendall(to_send) # Sending the current time to the client

while True:
    connectionSocket, address = serverSocket.accept()
    Thread(target=handle_client, args=()).start() # Applying the multi-threading mechanism to process multiple client requests sent at the same time 

# import socket
# from _thread import *
# import threading
# print_lock = threading.Lock()

# # thread function
# def threaded(c):
# 	while True:
# 		receive=c.recv(1024).decode('utf-8')
# 		if not received:
# 			print("Closing Connection")
# 			print_lock.release()
# 			break
# 		to_send=str(time.time()).encode('utf-8')
# 		c.send(to_send)
# 	# connection closed
# 	c.close()


# def Main():
#     serverPort = 1234
# 	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	s.bind(('', serverPort))
# 	print("socket binded to port", serverPort)

# 	s.listen(5)
# 	print("socket is listening")

# 	while True:
# 		c, addr = s.accept()
# 		print_lock.acquire()
# 		print('Connected to :', addr[0], ':', addr[1])
# 		start_new_thread(threaded, (c,))
# 	s.close()


# if __name__ == '__main__':
# 	Main()
