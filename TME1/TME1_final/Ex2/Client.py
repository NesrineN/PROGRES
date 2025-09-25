from socket import *
import time
from datetime import datetime

def runclient(n, servername):
    '''
    input: 
        n: number of requests
        serverName: the IP address of the server
    '''
    print("running client with {} requests".format(n))
    serverPort = 1234
    
    for i in range(n):
        clientSocket = socket(AF_INET,SOCK_STREAM) # Creating the client socket
        delay = 2.0
        clientSocket.settimeout(delay) # setting a timeout of 2 seconds after which the client stops waiting for a response from the server
        try:
            clientSocket.connect((servername,serverPort)) # Connecting to the server via the handshake TCP Protocol
        # Catching all types of errors that may occur    
        except ConnectionRefusedError: 
            print("Connection refused")
            exit()
        except TimeoutError: 
            print("Time Out Error!")
            exit()
        except gaierror: # if the IP address is written in a wrong format
            print("This host does not seem to exist!")
            exit()
        except:
            print("Something went wrong!")
            exit()
        message = ('Request current time').encode('utf-8')
        delay = 0.4 # sec
        while True:
            clientSocket.sendall(message) # the whole message to be sent at once
            clientSocket.settimeout(delay)
            try:
                print("trying to send a request")
                modifiedMessage = clientSocket.recv(2048).decode('utf-8') # Receiving the current time on the server machine 
            except TimeoutError:
                delay = delay *2 #  increasing the delay time each time we dont receive a response
                if delay > 2.0: # if delay reaches 2 seconds , exit program
                    print('Time out Error!')
                    exit()
            except:
                print("Something went wrong!")
                exit()
            else:
                break
            
        
        # end = time.time()
        
        now = datetime.now()
        print(now)
        current_time = now.strftime("%H:%M:%S")
        end = datetime.strptime(current_time, "%H:%M:%S") 
        print(end)
        # newMessage = float(modifiedMessage)
        print(modifiedMessage) # parsing string to float to calculate time difference
        # print(modifiedMessage)
        print("The Clock difference between the server and this machine is: ",end - newMessage)
        clientSocket.close() # Closing the client socket
    
def main():
    n = input("Please enter the number of requests you want to make to the server.\nEnter number here:")

    try:
        while(int(n)<=0):
            n=input("Please enter a number greater than 0\nEnter your number here: ")

        n_int = int(n)
    except ValueError:
        # Handle the exception
        print("You did not enter an integer")
    sname=input("Please enter the server name you would like to contact:")
    runclient(n_int, sname)

if __name__ == "__main__":
    main()