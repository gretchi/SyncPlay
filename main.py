#!/usr/bin/env python3

import socket


BROADCAST_PORT = 39229
SESSION_PORT = 39230


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(b"Hello, UDP BroadCast", ('', BROADCAST_PORT))
    sock.close()


if __name__ == "__main__":
    main()
