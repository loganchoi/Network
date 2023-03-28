#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
UDP echo with scapy instead of socket
"""
import time
import fake_time  # Use for time calcs
import sys
import statistics
from scapy.all import *

# https://scapy.readthedocs.io/en/latest/troubleshooting.html
conf.L3socket = L3RawSocket
# sometimes needed for default gateway, and
# always for localhost, and
# sometimes not for remote.


def parse_args() -> tuple[str, int, int, int]:
    """
    parses the 4 args:
    server_hostname, server_port, num_pings, timeout
    """
    return (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))


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

    pass  # delete this and write (or copy from pa03)


def main() -> None:
    SERVER_HOSTNAME, SERVER_PORT, NUM_PINGS, TIMEOUT = parse_args()
    rtt_hist = []
    SERVER_IP = "127.0.0.1"
    # Note: you will want exception handling for lost packets (think timeout)
    for x in range(0, NUM_PINGS):
        y = x + 1
        message = f"PING {SERVER_HOSTNAME} (127.0.0.1) {y} {time.asctime()}"
        bytes = len(message.encode())
        if x == 0:
            print("PING", SERVER_HOSTNAME, "(", end="")
            print(SERVER_IP, end="")
            print(")", bytes, "bytes of data.")
        try:
            start = fake_time.time()
            response = sr1(
                IP(dst="127.0.0.1")
                / UDP(dport=SERVER_PORT, sport=12001)
                / message.encode(),
                timeout=TIMEOUT,
                verbose=0,
            )
            if "oops" in response.payload[UDP].load.decode():
                print("Damaged packet")
                end = fake_time.time()
                rtt_hist.append((end - start) * 1000)
            else:
                end = fake_time.time()
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
