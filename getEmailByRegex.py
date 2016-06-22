import re

def is_email(input):
	pattern = r"([\w._]+)@([\w_\-.]+?)"
	match = re.match(pattern, input)
	if match:
		return True
	else:
		return False 

def get_emails(paragraph):
	pattern = r"[\w._]+@[\w_\-.]+"
	matches = re.findall(pattern, paragraph)
	return matches
		

def get_accounts(paragraph):
	pattern = r"([\w._]+)@[\w_\-.]+"
	matches = re.findall(pattern, paragraph)
	return matches


