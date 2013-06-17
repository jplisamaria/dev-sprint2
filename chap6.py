# Enter your answrs for chapter 6 here
# Name:Lisa-Maria Mehta


# ******************
# ** Exercise 6.6 **
# ******************
# Palindrome: Function definitions
# ----------------------------------

def first(word):
	"""Returns first element of a string"""
	return word [0]

def last(word):
	"""Returns last element of a string"""
	return word [-1]

def middle(word):
	"""Takes a string as an argument, and returns same string
	with the first and last elements truncated off."""
	return word [1:-1]


def is_palindrome (word):
	"""Takes a string as an argument. Exits if the 
	string has 0 length.  Returns True if it is a palindrome,
	and False if it is not a palindrome."""
	if len(word) == 0:
		return
	if (len(word) == 1) or ((len(word)==2) and (first(word)==last(word))):
		return True
	else:
		if first(word) != last (word):
			return False
		return is_palindrome(middle(word))


# ------------------------
# Palindrome: Main Program
# ------------------------

print "Enter word (case matters):",
word = raw_input ()

if is_palindrome(word) == True:
	print word, "is a palindrome."
elif is_palindrome(word) == False:
	print word, "is not a palindrome."
else:
	print "Error: This is not a word."







# ******************
# ** Exercise 6.8 **
# ******************
# Greatest Common Divisor
# -------------------------------------------------
import math

def GCD (a,b):
	"""Takes 2 inputs, and returns their GCD"""
	#determine which integer is more massive, and call the integer with the  
	#larger absolute value 'n' for numerator and other one 'd' for denominator
	if math.fabs(a)>=math.fabs(b):
		n = a 
		d = b
	else:
		n = b
		d = a
	## Base case if one of the integers is 0
	if d == 0:
		return n	
	## General case	
	R = n % d
	if R == 0:
		return int(math.fabs(d))
	else:
		return GCD (d,R)

print
print "Enter two integers to find GCD"
print "First integer:",
a = raw_input()
print "Second integer:",
b = raw_input()

print "GCD for", int(a) , "and", int(b) , "is:",
print GCD (int(a),int(b))