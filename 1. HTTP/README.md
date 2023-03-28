# Programming assignment 1 (pa01)
Welcome to the World Wide Web (HTTP)

![](ithinkthereforeiam.png)

## Deliverables
* `web_server.py`
* `iactuallytestedthis-web_server.png`
* `client_browser.py`
* `iactuallytestedthis-client_browser.png`
* `report.md`

## Details
* Finish / fill in your python server `web_server.py` and write the client `client_browser.py`.
* Include screenshots of you how you ran the code, with your web browser and termials displaying the results.
* All source and text files should be utf-8 with Unix delimiters, written in Python3.

## Hints
* If you want to know what a browser request looks like, for example, just open Wireshark, and user you actual browser and observe its requests.
* Have fun!

## Part 1: You code a simple Web server
In this lab, you will learn the basics of socket programming for TCP connections in Python: how to create a socket, bind it to a specific address and port, as well as send and receive a HTTP packet.
You will also learn some basics of HTTP header format.
You will develop a web server that handles client requests.
Your web server should:
* accept and parse the HTTP request, 
* get the requested file from the server's file system, 
* create an HTTP response message consisting of the requested file preceded by header lines, and then 
* send the response directly to the client.
* If the requested file is not present in the server, the server should send an HTTP "404 Not Found" message back to the client.

### Code
You will find the skeleton code for the Web server in the repo.
You are to complete the skeleton code.
The places where you need to fill in code are marked with `pass`
Each place may require one or more lines of code.

### Running the Server
There are some an HTML files (e.g., `hello_world.html`) in the `web_files/` directory
Run the server program.
Determine the IP address of the host that is running the server (e.g., 128.238.251.26). 
From another host, open a browser and provide the corresponding URL. For example:

`http://128.238.251.26:6789/hello_world.html`

Note also the use of the port number after the colon.
You need to replace this port number with whatever port you have used in the server code.
In the above example, we have used the port number 6789.
The browser should then display the contents of `hello_world.html`.
If you omit ":6789", the browser will assume port 80, and you will get the web page from the server only if your server is listening at port 80.
Then try to get a file that is not present at the server. 
You should get a "404 Not Found" message, and return the 404 file.

This first part will get you some points, independent of whether you complete the next section!

## Part 2: Multi-thread the server
Use multithreaded on your server so that is capable of serving multiple requests simultaneously.
Using threading, first create a main thread in which your modified server listens for clients at a fixed port.
When it receives a TCP connection request from a client, it will set up the TCP connection through another port and services the client request in a separate thread.
There will be a separate TCP connection in a separate thread for each request/response pair.

## Part 3: You code a simple Web browser
Instead of using a browser, write your own HTTP client to test your server, and query from websites.
Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output.
You can assume that the HTTP request sent is a GET method.
The client should take command line arguments specifying the server IP address or host name, the port at which the server is listening, and the path at which the requested object is stored at the server.
The following is an input command format to run the client.

`client_browser.py server_host server_port filename`

## Part 4: write up
Write a `report.md` which includes
* the above 3 screenshots, so that they are visible in the git-classses web interface, and 
* descriptions of each screenshot
* notes about your setup.
