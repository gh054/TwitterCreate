import random
from splinter import Browser

# BELOW: ALL FUNC DEFINITIONS

def main():
	print "********************************************************"
	print "Hello and welcome to my Twitter account generator"
	print "author: gh054"
	print ""
	print ""
	print "Features:"
	print "1. Generate Usernames"
	print "2. Generate Passwords"
	print "3. Generate Emails"
	print "4. Create Twitter Accounts"
	print ""
	print ""
	print "********************************************************"
	print ""
	print ""
	proceed = raw_input("Type in a number from the Features list to continue: ")
	if (proceed == "1"):
		generateUsers()
	elif (proceed == "2"):
		generatePasses()
	elif (proceed == "3"):
		generateEmails()
	elif (proceed == "4"):
		twitterMagic()
	else:
		print "Program closing..."
		return 0;


def generateUsers():
	inputnum = input("How Many Usernames to Generate? ")
	print "Generating Users..."
	x = 0
	while (x < inputnum):
		# list generating here
		alphabet = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		# Username is always 8 chars (5 letters and 3 numbers)
		firstchar = random.choice(alphabet)
		secondchar = random.choice(alphabet)
		thirdchar = random.choice(alphabet)
		fourthchar = random.choice(alphabet)
		fifthchar = random.choice(alphabet)
		firstnum = random.choice(numbers)
		secondnum = random.choice(numbers)
		thirdnum = random.choice(numbers)
		userarr = [firstchar, secondchar, thirdchar, fourthchar, fifthchar, firstnum, secondnum, thirdnum]
		#print userarr
		# convert all vars to strings to call join() func
		finalUser = ''.join(str(e) for e in userarr)
		print finalUser
		# append mode so data can be added in each loop without overwriting
		fusers.write(finalUser+'\n')
		#print "Dumping Users to file..."
		# dump arrays to txt files
		x = x + 1
	cleanup()

def generatePasses():
	inputnum = input("How Many Passwords to Generate? ")
	print "Generating Passes..."
	x = 0
	while (x < inputnum):
		# list generating here
		alphabet = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		# Username is always 8 chars (5 letters and 3 numbers)
		firstchar = random.choice(alphabet)
		secondchar = random.choice(alphabet)
		thirdchar = random.choice(alphabet)
		fourthchar = random.choice(alphabet)
		fifthchar = random.choice(alphabet)
		firstnum = random.choice(numbers)
		secondnum = random.choice(numbers)
		thirdnum = random.choice(numbers)
		passarr = [firstchar, secondchar, thirdchar, fourthchar, fifthchar, firstnum, secondnum, thirdnum]
		#print userarr
		# convert all vars to strings to call join() func
		finalPass = ''.join(str(e) for e in passarr)
		print finalPass
		# append mode so data can be added in each loop without overwriting
		fpasses.write(finalPass+'\n')
		#print "Dumping Users to file..."
		# dump arrays to txt files
		x = x + 1
	cleanup()


def generateEmails():
	inputnum = input("How Many Emails to Generate? ")
	print "Generating Emails..."
	x = 0
	while (x < inputnum):
		alphabet = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		firstchar = random.choice(alphabet)
		secondchar = random.choice(alphabet)
		thirdchar = random.choice(alphabet)
		fourthchar = random.choice(alphabet)
		fifthchar = random.choice(alphabet)
		firstnum = random.choice(numbers)
		secondnum = random.choice(numbers)
		thirdnum = random.choice(numbers)
		ataoldotcom = "@aol.com"
		emailarr = [firstchar, secondchar, thirdchar, fourthchar, fifthchar, firstnum, secondnum, thirdnum, ataoldotcom]
		finalEmail = ''.join(str(e) for e in emailarr)
		print finalEmail
		femails.write(finalEmail+'\n')
		x = x + 1
	cleanup()


def twitterMagic():
	print "Twitter Magic Time!!!"
	browser = Browser('firefox')
	browser.visit('https://twitter.com/signup')
	nameslist = grabNames()
	emaillist = grabEmails()
	passlist = grabPasses()
	userlist = grabUsers()
	# for each name in the list, fill the form in with data from the text files
	# note to self - you have to set variables to loop through and pick the next name after the first is signed up
	# STEPS!!!
	# fill name field
	# fill email
	# fill password
	# uncheck check mark
	# click signup button
	# (NEXT PAGE)
	# fill username?
	# profit
	x = 0
	for x in nameslist:
		browser.fill(nameslist[x], 'full-name')
		browser.fill(emaillist[x], 'email')
		browser.fill(passlist[x], 'password')
		browser.fill(userlist[x], 'username')
		browser.uncheck('checkbox')
		browser.find_by_name('Sign Up').first.click()
		browser.back()
		x = x + 1


def grabNames():
	returnThisList = []
	for line in fnames:
		returnThisList.append(line)

def grabEmails():
	returnThisList = []
	for line in femails:
		returnThisList.append(line)

def grabPasses():
	returnThisList = []
	for line in fpasses:
		returnThisList.append(line)

def grabUsers():
	returnThisList = []
	for line in fusers:
		returnThisList.append(line)

def cleanup():
	print "Cleaning up..."
	fusers.close()
	fpasses.close()
	fnames.close()
	femails.close()
	print "Done cleanup() function. Now closing..."

# ******************************************************************************************************
fnames = open("twitter-fullnames", "a+")
femails = open("twitter-emails", "a+")
fpasses = open("twitter-pass", "a+")
fusers = open("twitter-user", "a+")
main()
# ******************************************************************************************************
