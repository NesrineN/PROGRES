from socket import *
import time

def main():
    n = input("Please enter the number of requests you want to make to the server.\nEnter number here:")
    try:
        while(int(n)<=0):
            n=input("Please enter a number greater than 0\nEnter your number here: ")

        n_int = int(n)
        sname=input("Please enter the server name you would like to contact:")
        runclient(n_int, sname)
    except ValueError:
        # Handle the exception in case the user does not enter an integer
        print("You did not enter an integer")

def runclient(n, serverName):
    '''
    input: 
        n: number of requests
        serverName: the IP address of the server
    '''
    print("running client with {} requests".format(n))
    serverPort = 1232
    sumRTT = 0
    for i in range(n):
        clientSocket = socket(AF_INET,SOCK_DGRAM) # Creating the client socket
        message = ('1').encode('utf-8')
        start = time.time()
        delay = 0.2 # sec
        while True:
            try:
                clientSocket.sendto(message,(serverName,serverPort)) # sending request to the server
                clientSocket.settimeout(delay) # setting a timeout to the request
            # Catching all types of errors that may occur    
            except gaierror: # if the IP address is written in a wrong format
                print("This host does not seem to exist!")
                exit()
            except:
                print("Something went wrong!")
                exit()
            try:
                print("trying to send a request")
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            except TimeoutError:
                delay = delay *2 # increasing the delay time each time we dont receive a response
                if delay > 2.0: # if delay reaches 2 seconds , exit program
                    print('server seems down')
                    exit()
            except:
                print("Something went wrong!")
                exit()
            else:
                break
        
        end = time.time()
        print("RTT of request number ",i+1,"is: ",end-start)
        sumRTT += end - start # getting the sum of RTTs of all requests
        clientSocket.close() # closing the connection

    print("Average RTT: ", sumRTT/(i+1)) # Averaging the RTTs obtained

if __name__ == "__main__":
    main()