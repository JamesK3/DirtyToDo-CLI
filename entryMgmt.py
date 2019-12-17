#!/usr/bin/env python3

import re

def list():
    tellMe = "blue"
    while not re.search(r"x",tellMe):
        tellMe = input("How you doin!?!")
