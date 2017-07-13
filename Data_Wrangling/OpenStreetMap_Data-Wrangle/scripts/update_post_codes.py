## Updates Post Codes if they have incorrect values

# Updates Post Codes
def update_code(element):
	# Finds Post Codes that are not correctly formatted
	post_code = 0
	if element.tag == 'tag':
		attribute = element.get('k')
		if attribute == 'addr:postcode':
			post_code = element.get('v')
			return post_code
			if len(post_code) > 5:
				if '-' in post_code:
					return post_code[:5]
			else:
				return post_code