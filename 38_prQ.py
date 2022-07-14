# Python function that accepts a string and calculates the number of uppercase and lowercase letters for

# Python3 program to count upper and
# lower case characters without using
# inbuilt functions
def upperlower(string):

	upper = 0
	lower = 0

	for i in range(len(string)):
		
		# For lower letters
		if (ord(string[i]) >= 97 and
			ord(string[i]) <= 122):
			lower += 1

		# For upper letters
		elif (ord(string[i]) >= 65 and
			ord(string[i]) <= 90):
			upper += 1

	print('Lower case characters = %s' %lower,
		'Upper case characters = %s' %upper)

# Driver Code
string = 'My name is Tejal Prakash Pathak'
upperlower(string)


# o/p:
# Lower case characters = 22 Upper case characters = 4
# PS F:\Coding Practise\GTT Python Training>