# this program is for validating the data.

# This is the simple program for ZeroMQ module with Pushing other server.

import sys
import time
import zmq
import json
import traceback


class TransfromData():
	"""	A Declarative class for data validations """

	def __init__(self, args):
		self.GetData(args)

	def GetData(self,format_data):
		""""""
		while True:
			# load_data = receiver.recv()
			# format_data = json.loads(load_data)
			valid_data = Validation(format_data)

			# Calling methods to validate the data
			mbr_id = valid_data.validate_mbr_id()
			f_name = valid_data.validate_mbr_first_name()
			l_name = valid_data.validate_mbr_last_name()
			addrs = valid_data.validate_mbr_address()
			city = valid_data.validate_mbr_city_name()
			phone = valid_data.validate_mbr_phone()
			email = valid_data.validate_mbr_email()
			dob = valid_data.validate_mbr_birth_date()
			
			try:
				if mbr_id and f_name and l_name and addrs and city and phone and dob and email:
					print "sending to loader %s msg: " % format_data

					# Sending the data to store in Session i.e., DB
					context = zmq.Context()
					sink = context.socket(zmq.PUSH)
					sink.connect("tcp://localhost:5558")
					sink.send(json.dumps(format_data))
				else:
					print "validation fail"
			except Exception, e:
				exce_trace = traceback.format_exc()
				print exce_trace
				print e.__class__.__name__

class Validation():
    def __init__(self, arg):
        self.data = arg		

    def validate_mbr_id(self):
    	""" Method to validate Member ID """
    	if self.data['MEMBER_ID']:
    		return True
    	else:
    		print "Member ID is missing in CSV File"
    		print False

    def validate_mbr_first_name(self):
    	""" Method to validate Member First Name"""
        if self.data['FIRST_NAME']:
        	if len(self.data['FIRST_NAME']) <= 32:
        	    return True
        	else:
        		print "Member First Name length is greater than 32 Characters"
        else:
            print "Member First Name is missing in CSV File"
            return False


    def validate_mbr_last_name(self):
    	""" Method to validate Member First Name"""
    	if self.data['LAST_NAME']:
        	if len(self.data['LAST_NAME']) <= 32:
        		return True
        	else:
        		print "Member First Name length is greater than 32 Characters"
        else:
        	print "Member Lirst Name is missing in CSV File"
        	return False
    
    def validate_mbr_address(self):
    	""" Method to validate Member First Name"""
    	if self.data['ADDRESS']:
        	if len(self.data['ADDRESS']) <= 32:
        		return True
        	else:
        		print "Member ADDRESS length is greater than 32 Characters"
        else:
        	print "Member ADDRESS is missing in CSV File"
        	return False


    def validate_mbr_city_name(self):
    	""" Method to validate Member First Name"""
    	if self.data['CITY']:
        	if len(self.data['CITY']) <= 32:
        		return True
        	else:
        		print "Member CITY length is greater than 32 Characters"
        else:
        	print "Member CITY is missing in CSV File"
        	return False


    def validate_mbr_phone(self):
    	""" Method to validate Member First Name"""
    	if self.data['PHONE']:
    		return True
    	else:
    		print "Member Phone is missing in the CSV File."
    		print False	


    def validate_mbr_email(self):
    	""" Method to validate Member First Name"""
    	if self.data['EMAIL']:
    		return True
    	else:
    		print "Member Email is missing in the CSV file"
    		return False

    def validate_mbr_birth_date(self):
    	""" Method to validate Member First Name"""
    	if self.data['DOB']:
    		return True
    	else:
    		print "Member Data of Birth is missing in the CSV File."
    		return False

if __name__ == "__main__":
    """
    """
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://127.0.0.1:5558")
    reveived_data = receiver.recv()
    load_data = json.loads(reveived_data)
    TransfromData(load_data)