# PA03 - UDP echo

![](echo.jpg)

## Background
* Read about ping: https://en.wikipedia.org/wiki/Ping_(networking_utility)
    ```bash
    whatis ping
    which ping
    man ping
    ping --help
    ping 127.0.0.1
    ping google.com
    ```

* Enjoy learning about this entertaining ping gimick:
https://www.youtube.com/watch?v=JcJSW7Rprio

* See https://www.rfc-editor.org/rfc/rfc792 section on echo request and reply:

Echo or Echo Reply Message
```
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Type      |     Code      |          Checksum             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Identifier          |        Sequence Number        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Data ...
+-+-+-+-+-
```

IP Fields:

Addresses

  The address of the source in an echo message will be the destination of the echo reply message.
  To form an echo reply message, the source and destination addresses are simply reversed, the type code changed to 0, and the checksum recomputed.

Type

  8 for echo message;

  0 for echo reply message.

Code

  0

Checksum

  The checksum is the 16-bit ones's complement of the one's complement sum of the ICMP message starting with the ICMP Type.
  For computing the checksum, the checksum field should be zero.
  If the total length is odd, the received data is padded with one octet of zeros for computing the checksum.
  This checksum may be replaced in the future.

Identifier

  If code = 0, an identifier to aid in matching echos and replies, may be zero.

Sequence Number

 If code = 0, a sequence number to aid in matching echos and replies, may be zero.

   Description

      The data received in the echo message must be returned in the echo reply message.

      The identifier and sequence number may be used by the echo sender to aid in matching the replies with the echo requests.
      For example, the identifier might be used like a port in TCP or UDP to identify a session, and the sequence number might be incremented on each echo request sent.
      The echoer returns these same values in the echo reply.

      Code 0 may be received from a gateway or a host.

If you forget about how echo requests work, just wait, it'll come back to you!

## Introduction
Ping uses IP-layer messages and raw sockets, so we won't program real ping yet.
This assignment both 1) gets you practice using UDP, and 2) is practice for the network layer, which we're doing now.
In this lab, you will learn the basics of socket programming for UDP in Python.
You will learn how to send and receive datagram packets using UDP sockets and also, how to set a proper socket timeout.
Throughout the lab, you will gain familiarity with a application implementing `ping` and its usefulness in computing statistics such as packet loss rate.
You will first study a simple internet ping server written in the Python, and implement a corresponding client.
The functionality provided by these programs is similar to the functionality provided by standard ping programs available in modern operating systems.
However, these programs use UDP, rather than the standard Internet Control Message Protocol (ICMP) within IP, to communicate with each other.
The ping protocol allows a client machine to send a packet of data to a remote machine, and have the remote machine return the data back to the client unchanged (an action referred to as echoing).
Among other uses, the ping protocol allows hosts to determine round-trip times to other machines.
You are given the complete code for the Ping server below. Your task is to write the Ping client.

## Provided files
`udp_echo_server.py` is already working, and is provided to you.

## Deliverables
Submit these files/edits:
* `udp_echo_client.py`
* `report.md` which includes markdown-embedded images of how you ran your code, and what success looked like, along with any brief notes you want me to know.
* You will hand in the complete client code and screenshots at the client verifying that your echo program works as required.

## Server Code
The given server code fully implements an echo server.
You do not need to modify this code.
In this server code, 30% of the client's packets are simulated to be lost.
You should study this code carefully, as it will help you write your echo client.
The server sits in an infinite loop listening for incoming UDP packets.
When a packet comes in, the server simply sends it back to the client.

## Packet Loss
UDP provides applications with an unreliable transport service.
Messages may get lost in the network due to router queue overflows, faulty hardware or some other reasons.
Because packet loss is rare, or even non-existent, in typical campus networks, the server in this lab injects artificial loss to simulate the effects of network packet loss.
The server creates a randomized integer variable, which determines whether a particular incoming packet is lost or not.
Ideally, you would use exception handling and catching of those exceptions to handle packet loss.

## Client Code
You need to implement the following client program.
The client should send 10 pings to the server.
Because UDP is an unreliable protocol, a packet sent from the client to the server may be lost in the network, or vice versa.
For this reason, the client cannot wait indefinitely for a reply to a ping message.
You should program the client to wait up to one second for a reply; 
if no reply is received within one second, your client program should assume that the packet was lost during transmission across the network.
You will need to look up the Python3 documentation to find out how to set the timeout value on a datagram socket.

### Specifically, your client program should
1. Send the ping message using UDP.
Note: Unlike TCP, you do not need to establish a connection first, since UDP is a connectionless protocol.
2. Print the response message from server, if any.
3. Calculate and print the round trip time (RTT), in seconds, of each packet, if server responses.
4. Otherwise, print an error (see output files).
5. At the end, you will need to report the RTT statistics, at the end of all pings from the client.

During development, you should run the server on your machine, and test your client by sending packets to localhost (or, 127.0.0.1).
After you have fully debugged your code, you should see how your application communicates across the network with the ping server and ping client running on different virtual machines.

### Message Format
The ping messages in this lab are formatted in a simple way (given in the code), something like this:
```py
message = f"PING {SERVER_HOSTNAME} ({SERVER_IP}) {PING_NUM} {time.asctime()}"
```

### random things to watch out for
Watch out for off-by-one errors with size.
Think about the numbe of times you call the time function (which is a fake time function...)

I hope you have a resounding sucess with this assignment...
