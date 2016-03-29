# This is the simple program for ZeroMQ module with Requesting other server.

# Imports
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

# This is localhost server port.
socket.connect("tcp://127.0.0.1:5000")
 
for i in range(10):
    msg = "msg %s" % i
    socket.send(msg)
    print "Sending", msg
    msg_in = socket.recv()
