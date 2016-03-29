# This is the simple program for ZeroMQ module with Pushing other server.

import zmq
import random
import time
 
context = zmq.Context()
 
 
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")
 
random.seed()
 
while True:
    workload = random.randint(1, 100)
    sink.send(str(workload))
