#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Mimic ICMP traceroute with scapy
"""
import time
from scapy.all import *

# https://scapy.readthedocs.io/en/latest/troubleshooting.html
conf.L3socket = L3RawSocket
# sometimes needed for default gateway, and
# always for localhost, and
# sometimes not for remote.

SERVER_HOSTNAME = "bad.horse"
MAX_HOPS = 30
TIMEOUT = 5
pass  # delete this and write
