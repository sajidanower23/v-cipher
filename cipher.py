#Function names are in underscore naming
#function arguments are in camelCase

def get_length(cipherText):

	print "The length of the cipher text is " + str(len(cipherText))
	for shift in range(1, len(cipherText)):
		print shift_compare(cipherText, shift)


# Compares the cipherText with a version of it shifted by shiftLength
def shift_compare(cipherText, shiftLength):
	assert(shiftLength <= len(cipherText))
	numMatch = 0
	totalLength = len(cipherText)
	for shiftIndex in range(shiftLength, totalLength):
		if(cipherText[shiftIndex] == cipherText[shiftIndex - shiftLength]):
			# print "{} and {} match".format(cipherText[shiftIndex], cipherText[shiftIndex - shiftLength])
			numMatch += 1

	return numMatch

cipherText = raw_input("Enter the cipher text: ")
get_length(cipherText)


# 0 1 2 3 4 5 len 
# a b c d e f -> cipherText
#   a b c d e 1
#     a b c d 2
#       a b c 3
#         a b 4
#           a 5

# for i in range(shiftLength, totalLength)
# 	compare cipherText[i] and cipherText[i - shiftLength]