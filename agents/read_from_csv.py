# this program is for reading the data from the CSV and sending them to validate.

import csv
import os

# Imports for Sending the data through ZeroMQ
import zmq
import random
import time

import json
 
context = zmq.Context()
 
 
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")
 
class ReaderData():

	def csv_dict_reader(csv_file):
	    """
	    Read a CSV file using csv.DictReader
	    """
	    try:
	    	reader = csv.DictReader(csv_file, delimiter=',')
	    	for line in reader:
	    		json_string = json.dumps(line)
	    		sink.send(json_string)

	    except IOError as (errno, strerror):
	    	print("I/O error({0}): {1}".format(errno, strerror))
	    return


	if __name__ == "__main__":
	    # with open("member_details_data.csv") as f_obj:
	    #     csv_dict_reader(f_obj)
		currentPath = os.getcwd()
		csv_file = os.path.join(currentPath, "member_details_data.csv")
		with open(csv_file) as f_obj:
			csv_dict_reader(f_obj)