# This is the simple program for ZeroMQ module with Pushing other server.

import sys
import time
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://127.0.0.1:5558")

while True:
    print receiver.recv()

