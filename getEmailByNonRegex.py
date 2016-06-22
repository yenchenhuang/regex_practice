def is_email(input):
	atIdx = input.find("@")
	if atIdx < 1:
		return False
	if " " in input:
		return False
	dotIdx = input.find(".")
	if dotIdx <= atIdx+1:
		return False
	if dotIdx == len(input) - 1:
		return False
	return True

def get_emails(paragraph):
	candidates = paragraph.split(' ')
	emails = []
	for i in range(len(candidates)):
		if is_email(candidates[i]):
			emails.append(candidates[i])
	return emails

def get_accounts(paragraph):
	candidates = paragraph.split(' ')
	accounts = []
	for i in range(len(candidates)):
		if is_email(candidates[i]):
			atIdx = candidates[i].find("@")
			accounts.append(candidates[i][:atIdx])
	return accounts

