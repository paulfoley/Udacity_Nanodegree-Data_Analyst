# Python script to determine if string is number or words

def is_number(s):
	# Determines if input is a string or number
	try:
		float(s)
		return True
	except ValueError:
		return False