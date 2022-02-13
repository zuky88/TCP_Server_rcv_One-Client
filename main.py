#!/usr/bin/env python3

import time
import threading
import sys
import server
import clientA

def main_thread():
    server.thread_start()
    time.sleep(3)
    clientA.thread_start()

if __name__ == '__main__':
    try:
        t = threading.Thread(target = main_thread,args=())
        t.setDaemon(True)
        t.start()
        while True:
            c = sys.stdin.read(1)
            if c == 'q':
                sys.exit()
    except KeyboardInterrupt:
        server.server.close()
        clientA.server.close()
        print('[main]Socket close.')
        sys.exit(1)

