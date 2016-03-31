# this program is for validating the data.

# This is the simple program for ZeroMQ module with Pushing other server.

import sys
import time
import zmq
import json


class TransfromData():
	"""
	"""

	def DataReceive(receiver):
		"""
		"""
		while True:
			load_data = receiver.recv()
			format_data = json.loads(load_data)
			print format_data
			
			# Validating the data to send to session

	if __name__ == "__main__":
		context = zmq.Context()

		receiver = context.socket(zmq.PULL)
		receiver.bind("tcp://127.0.0.1:5558")
		DataReceive(receiver)