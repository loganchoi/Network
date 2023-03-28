#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
UDP-echo program
Student template.
"""
import socket
import time
import sys
import statistics


def parse_args() -> tuple[str, int, int, int]:
    """
    parses the 4 args:
    server_hostname, server_port, num_pings, timeout
    """
    return (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    pass  # delete this and write your code


def create_socket(timeout: int) -> socket.socket:
    """Create IPv4 UDP client socket"""
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    client.settimeout(timeout)
    return client
    pass  # delete this and write your code


def net_stats(
    num_pings: int, rtt_hist: list[float]
) -> tuple[float, float, float, float, float]:
    """
    Computes statistics for loss and timing.
    Mimicks the real ping's statistics.
    Check them out: `ping 127.0.0.1`
    See `man ping` for definitions.
    """
    loss = (1 - len(rtt_hist) / num_pings) * 100
    rtt_min = "{:.3f}".format(min(rtt_hist))
    rtt_max = "{:.3f}".format(max(rtt_hist))
    rtt_mdev = "{:.3f}".format(statistics.stdev(rtt_hist))
    rtt_avg = "{:.3f}".format(sum(rtt_hist) / len(rtt_hist))
    return (loss, float(rtt_min), float(rtt_avg), float(rtt_max), float(rtt_mdev))
    pass  # delete this and write your code


def main() -> None:
    SERVER_HOSTNAME, SERVER_PORT, NUM_PINGS, TIMEOUT = parse_args()
    SERVER_IP = socket.gethostbyname(SERVER_HOSTNAME)
    client_socket = create_socket(timeout=TIMEOUT)
    client_socket.connect((SERVER_HOSTNAME, SERVER_PORT))
    rtt_hist = []
    # Note: you will want exception handling for lost packets (think timeout).
    for x in range(0, NUM_PINGS):
        y = x + 1
        message = f"PING {SERVER_HOSTNAME} ({SERVER_IP}) {y} {time.asctime()}"
        bytes = len(message.encode())
        start = time.time()
        if x == 0:
            print("PING", SERVER_HOSTNAME, "(", end="")
            print(SERVER_IP, end="")
            print(")", bytes, "bytes of data.")
        try:
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            end = time.time()
            if "oops" in data.decode():
                print("Damaged packet")
                rtt_hist.append((end - start) * 1000)
            else:
                print(bytes, "bytes from", SERVER_HOSTNAME, "(", end="")
                print(SERVER_IP, end="")
                print("): ping_seq=", end="")
                print(y, "time=", end="")
                print("{:.3f}".format((end - start) * 1000), "ms")
                rtt_hist.append((end - start) * 1000)
        except:
            print("timed out")
    # ping stats
    loss, rtt_min, rtt_avg, rtt_max, rtt_mdev = net_stats(
        num_pings=NUM_PINGS, rtt_hist=rtt_hist
    )
    total = sum(rtt_hist)
    print()
    print("--- localhost ping statistics ---")
    print(
        NUM_PINGS,
        "packets transmitted,",
        len(rtt_hist),
        "received,",
        "{:.3f}".format(loss),
        end="%",
    )
    print(" packet loss, time", "{:.3f}".format(total), end="")
    print("ms")
    print("rtt min/avg/max/mdev =", rtt_min, end="/")
    print(rtt_avg, end="/")
    print(rtt_max, end="/")
    print(rtt_mdev, "ms")


if __name__ == "__main__":
    main()
