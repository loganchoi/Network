#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A simple Web server.
GET requests must name a specific file,
since it does not assume an index.html.
"""

import socket
import threading
import typing


def handler(conn_socket: socket.socket, address: typing.Tuple[str, int]) -> None:
    """
    Handles the part of the client work-flow that is client-dependent,
    and thus may be delayed (blocking program flow).
    """
    try:
        # Receives the request message from the client
        # Delete pass and write
        msg = conn_socket.recv(1024)
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        # Delete pass and write
        path = msg.decode().split()[1]
        # print(path)

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        # Read file off disk, to send
        # Store the content of the requested file in a temporary buffer
        # Delete pass and write
        file = open(path[1:], "r")
        buffer = file.read()

        # Send the HTTP response header line to the connection socket
        # Delete pass and write
        header = "HTTP/1.1 200 OK\r\n"
        conn_socket.send(header.encode())

        # Send the content of the requested file to the connection socket
        # Delete pass and write
        buffer = "\n" + buffer
        conn_socket.send(buffer.encode())

        file.close()

    except IOError:
        # Send HTTP response message for file not found (404)
        # Delete pass and write
        # print("IO ERROR IO ERROR")
        notFound = "HTTP/1.1 404 Not Found\r\n"
        conn_socket.send(notFound.encode())

        # Open file, store the content of the requested file in a temporary buffer
        # Delete pass and write
        npath = "web_files/not_found.html"
        nfile = open(npath, "r")
        buffer = nfile.read()
        # Send the content of the requested file to the connection socket
        # Delete pass and write
        buffer = "\n" + buffer
        conn_socket.send(buffer.encode())
        nfile.close()
    except:
        print("Bad request")
    finally:
        conn_socket.close()


def main() -> None:
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_port = 6789

    server_socket.bind(("", server_port))

    # Listen to at most 2 connection at a time
    # Server should be up and running and listening to the incoming connections
    # Delete pass and write
    server_socket.listen(2)

    threads = []
    try:
        while True:
            # Set up a new connection from the client
            # Delete pass and write
            c, addr = server_socket.accept()

            addr = tuple(addr)
            # call handler here, start any threads needed
            # Delete pass and write
            new_thread = threading.Thread(target=handler, args=(c, addr))
            new_thread.start()
            # Just to keep track of threads
            threads.append(new_thread)
    except:
        print("Exception occured (maybe you killed the server)")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
