## Script to Update Street Names

# Import Regular Expression Module
import re

# Mapping of Street Values
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
mapping = {"St" : "Street", "St." : "Street", "Rd." : "Road", "Rd" : "Road", "Ave" : "Avenue", "Blvd": "Boulevard", "Ct": "Court", "Dr": "Drive", "Pl": "Place"}

def update_name(name, mapping):
	# Updates Street Names
	match = street_type_re.search(name)
	if match:
		street_type = match.group()
		if street_type in mapping:
			name = re.sub(street_type, mapping[street_type], name)
	return name