# This is the simple program for ZeroMQ module with Replying other server.

# Imports
import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)

# Host that will reply to the requesting host.
socket.bind("tcp://127.0.0.1:5000")
 
# while True:
#     msg = socket.recv()
#     print "Got", msg
#     socket.send(msg)

while True:
    print  socket.recv()
