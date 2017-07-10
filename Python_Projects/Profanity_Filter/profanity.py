from urllib.request import urlopen

def read_text():
	quotes = open('text.txt')
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	return check_profanity(contents_of_file)

def check_profanity(text_to_check):
	with urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check) as url:
		output = url.read()
	if 'true' in output:
		return ('Profanity Alert!!')
	elif 'false' in output:
		return ('This document has no curse words!')
	else:
		return ('Could not scan the document properly.')

print(read_text())