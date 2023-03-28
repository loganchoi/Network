#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Your code tests start here:
# To debug in pudb3
# Highlight the line of code below below
# Type 't' to jump 'to' it
# Type 's' to 'step' deeper
# Type 'n' to 'next' over
# Type 'f' or 'r' to finish/return a function call and go back to caller
from convert_to_binary import convert_to_binary
import random

for _ in range(100):
    num = random.randint(0, 200)
    assert convert_to_binary(num) == bin(num)[2:]
