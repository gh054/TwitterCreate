import random

# BELOW: ALL FUNC DEFINITIONS

def main():
	print "********************************************************"
	print "Hello and welcome to my Twitter account generator"
	print "author: gh054"
	print ""
	print ""
	print ""
	print "Features:"
	print "1. Generate Usernames"
	print "2. Generate Passwords"
	print "3. Create Twitter Accounts"
	print "********************************************************"
	proceed = raw_input("Type in a number from the Features list to continue: ")
	if (proceed == "1"):
		generateUsers()
	elif (proceed == "2"):
		generatePasses()
	elif (proceed == "3"):
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

def twitterMagic():
	print "Twitter Magic Time!!!"

def cleanup():
	print "Cleaning up..."
	fusers.close()
	fpasses.close()

# ******************************************************************************************************
fusers = open("twitter-user", "a+")
fpasses = open("twitter-pass", "a+")
main()

# ******************************************************************************************************
