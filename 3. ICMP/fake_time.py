#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Fake time for autograding
"""
import random

random.seed(42)

faketime = 0.0


def time() -> float:
    global faketime
    faketime += random.random()
    return faketime
