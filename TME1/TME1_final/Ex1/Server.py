from socket import *
from numpy import random
serverPort = 1234

def runserver(port):
    print("running server 1")
    serverSocket = socket(AF_INET,SOCK_DGRAM) # Creating the UDP server socket
    serverSocket.bind(('',port)) # binding the socket to the port
    print("Server ready")

    while True:
        message, clientAddress = serverSocket.recvfrom(2048) # receiving request from the client
        modifiedMessage = message.decode('utf-8')
        serverSocket.sendto(modifiedMessage.encode('utf-8'),clientAddress) # sending back a response to the client

def runserverP(port, probability):
    '''
        Input:
            port: the specified port number
            probability: specifies the probability that the server responds to the client

    '''
    print("running server 2")
    serverSocket = socket(AF_INET,SOCK_DGRAM) # Creating the server socket and binding it to the port
    serverSocket.bind(('',port))
    print("Server ready")

    while True:
        print("I'm receiving from client")
        message, clientAddress = serverSocket.recvfrom(2048) # receiving request from the client
        number = random.randint(1,100) # returns a random integer between 1 and 100
        print(number)
        if number > probability: # send response to client if the random integer is greater than the probabilty
            modifiedMessage = 'hi, this is server'
            print("I'm returning ")
            serverSocket.sendto(modifiedMessage.encode('utf-8'),clientAddress)

def main():
    server = input("If you want to run the Server for exercises 1.1, 1.2, 1.3, Please enter 1.\nIf you want to run the Server for exercise 1.4, Please enter 2\nEnter your number here: ")
    try:
        while(int(server)!=1 and int(server)!=2):
            server=input("Please enter either 1 or 2!\nEnter your number here: ")

        server_int = int(server)
        if(server_int==1):
            runserver(serverPort)
        else:
            runserverP(serverPort,50)
    except ValueError:
        # Handle the exception
        print("You did not enter an integer")

if __name__ == "__main__":
    main()