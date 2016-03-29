# This is the simple program for ZeroMQ module with Requesting other server.

# Imports
import zmq
 
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5000")

# Commenting this line due to AttributeError: Socket has no such option: SOCKET
# socket.socket(zmq.SUBSCRIBE)

# Work Around.
# Messages starting with "netherlands" or "germany"

socket.setsockopt(zmq.SUBSCRIBE, "netherlands")
socket.setsockopt(zmq.SUBSCRIBE, "germany")


while True:
    print  socket.recv()
