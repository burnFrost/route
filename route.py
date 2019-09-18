#!/usr/bin/env python3

import struct, socket, webbrowser

def getRoute():
    with open("/proc/net/route") as y:
        for x in y:
            z = x.strip().split()
            if z[1] != '00000000' or not int(z[3], 16) & 2:
                continue
            return socket.inet_ntoa(struct.pack("<L", int(z[2], 16)))

print(getRoute())

route = "http://"+getRoute()

webbrowser.open(route, new=2)
