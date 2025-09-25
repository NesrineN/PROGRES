# Libraries Used: 
- socket
- os
- threading
- time

# Exercise 1
In this exercise, we started by creating a server and a client. 

In the server, we created 2 functions, the first creates a server for Ex 1.1, 1.2, and 1.3, the second function creates a different server for Ex 1.3. When Server.py is ran, depending on the input from the user the user decides whether we want to run server 1 for Ex 1.1, 1.2, 1.3 or server 2 for Ex 1.4.

In the client, we created a function runclient that takes as parameters the range n which is the number of requests that will be sent to the server, and the server's name. Both of those parameter will be input by the user when the Client.py file is run.

## 1. 
Here, we created a server (server function 1) and a client to send and receive requests. Using the UDP protocol, we want to code a PING mechanism. To do that, the client sent an arbitrary message to the server while calculating the time initially, and the time after it received the response. The server receives the request, and sends back an arbitrary response. 

For the RTT, the client sent multiple requests to the server and the average of the time elapsed was calculated by getting the sum of the time difference divided by the number of requests made by the client.

## 2.
For this part, we ran the files Server.py and Client.py on the same machine, and then, ran another Client.py file on another machine by connecting to the IP address of the machine where Server.py is. (we passed the servername as input when we ran Client.py)

In the Client.py file on a different machine:
We use ifconfig on cmd to get the IP address and then use this address as the server name input.

## 3.

For simultaneous requests, we opened multiple terminal windows and we ran the Client.py file on the separate windows at the same time. In each window, we gave a big range number (a different number of requests to be made by the different clients).

## 4.

In this exercise, we run the second server function created in the server.py file. 
Here, we modified the server by creating a random number that's either 0 or 1. The server responds to the request of the Client if the number is 1, and doesn't otherwise.
In that case, we can observe that when the server does not respond to the client, the client keeps on waiting for the server response forever. 

To work around that situation, we used the timeout mechanism with a specific delay so that if a client waits a certain amount of time with no response, the request keeps being sent until a specific threshold of delay is reached. After that, if there's no response, we catch the TimeoutError exception and close the program. 

We tested the code of this exercise on the same machine and on different machines as well similarly to how we did it in ex 1.2. We also made simultaneous requests on different terminal windows.

# Exercise 2
In this exercise, we started by creating a server and a client. 

In the server, we used a multi-threading TCP protocol so that the server could receive multiple requests from different clients sent at the same time.

In the client, we created a function runclient as well similarly to exercise 1 that takes as parameters the range n, the number of requests that will be sent to the server, and the server's name. Both of those parameter will be input by the user when the Client.py file is run.

## 1. 

Here, want to code a Clock difference mechanism. To do that, the client kept on sending requests to the server while calculating tha time initially. The server receives the request, and sends back the current time on the local machine.
After the client receives the response, it calculates the difference between the time sent by the server and the initial time calculated by the client.

## 2.

We tested the code on the same machine and on different machines the same way we did in Exercise 1.2.

## 3.

Similarly to Exercise 1.3, we opened multiple terminals, and ran multiple clients at the same time.

# Exercise 3

## 1. 

In this exercise, we created a Server.py file. We used a multi-threading TCP protocol as well.
The server then waits for requests to be made from the web browser. 
Once it receives a request, we used path module from the os library to manipulate the path we got from the browser.

Using the following code, we checked if the file exists. If it does, we sent back a modifiedMessage having a header with the status 200 OK to the web client, and the content which is the content of the file requested.

We tested the code using the following path as example:
127.0.0.1:1234/test.html where the html file can be find in the same directory as Server.py
```
if(os.path.exists(filepath)):
       content = open(filepath, "r").read()
       modifiedMessage = "HTTP/1.1 200 OK\r\n"
       modifiedMessage += "Content-Length: {}\r\n".format(len(content))
       modifiedMessage += "Content-Type: text/html\r\n\r\n"
       response = (modifiedMessage + content).encode("utf-8")
```

Using the following code, we sent to the web client a 404 Not found response with the content set to a 404 html file that we created in the same directory. This was done if the above condition is not met i.e. if the file requested does not exist:
```
else:
        content = open("404.html","r").read()
        modifiedMessage = "HTTP/1.1 404 Not Found\r\n"
        modifiedMessage += "Content-Length: {}\r\n".format(len(content))
        modifiedMessage += "Content-Type: text/html\r\n\r\n"
        response = (modifiedMessage+content).encode("utf-8")
```

## 2. & 3.

Similarly to what we've done in the previous Exercises, we tested the code on the same machine, on a different machine, and simultaneous requests.

We noticed that when making simultanous requests, one request gets processed instantaneously while the other keeps waiting.
