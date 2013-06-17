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
# Palindrome: Function definitions
# --------------------------------