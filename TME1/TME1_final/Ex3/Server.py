from socket import *
import os
from threading import *

serverPort = 1235
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('0.0.0.0',serverPort))
serverSocket.listen(1)
print('server ready')
def handle_client(clientSocket):
    while True:
        message = clientSocket.recv(2048).decode('utf-8') # receiving from client
        if not message:
            connectionSocket.close() # Closing the socket if nothing is received from the client
            break
        else:
            print(message)
        
            filepath=message.splitlines()[0].split(" ")[1][1:] # Splitting the URL string obtained from the web client and storing the file name requested in filepath
            if(os.path.exists(filepath)):
                content = open(filepath, "r").read() #reading the file if it exists and storing the content in content
                modifiedMessage = "HTTP/1.1 200 OK\r\n" # content will have a header , and the content of the file requested
                modifiedMessage += "Content-Length: {}\r\n".format(len(content))
                modifiedMessage += "Content-Type: text/html\r\n\r\n"
                response = (modifiedMessage + content).encode("utf-8")
                #    print(modifiedMessage)
            else:
                content = open("404.html","r").read() # Reading a 404 html file that we created in case the file does not exist in the current directory
                modifiedMessage = "HTTP/1.1 404 Not Found\r\n"
                modifiedMessage += "Content-Length: {}\r\n".format(len(content))
                modifiedMessage += "Content-Type: text/html\r\n\r\n"
                response = (modifiedMessage+content).encode("utf-8")
            print(modifiedMessage)
            connectionSocket.sendall(response) # Sending the response (header + content) to the client
while True:
    connectionSocket, address = serverSocket.accept()
    Thread(target=handle_client,args=(connectionSocket,)).start() # Applying the multi-threading mechanism to process multiple client requests sent at the same time 
    