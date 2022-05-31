#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for i in str:
        caps = ord(i)
        if ord('a') <= caps <= ord('z'):
            caps = caps - 32
        temp += chr(caps)
    print("{}".format(temp))
