# Enter your answrs for chapter 7 here
# Name: Lisa-Maria Mehta


# ******************
# ** Exercise 7.5 **
# ******************
# Aproximating pi using Ramunujan method
# -------------------------------------


## Could not get this to work until I specified that the numerator and 
## denominator had to be type float. Also, my method is 

import math

def estimate_pi():
	""" Estimates pi using Ramunujan method"""
	constant = (2 * math.sqrt(2)) / 9801

	pi_reciprocal_est = 0	# initial condition
	k= 0 					# initial condition
	sigma_formula = 0		# initial condition


	while True:
		numerator = float(math.factorial(4*k) * (1103 + 26390*k))
		denominator = float((math.factorial(k))**4) * (396**(4*k))
		sigma_temp = numerator/denominator
		sigma_formula = sigma_formula + sigma_temp
		pi_reciprocal_est = constant * sigma_formula
		if sigma_temp < 1e-15:
			print '"Last term" =', sigma_temp
			break
		k = k + 1
	print "k =", k
	return 1/pi_reciprocal_est




pie = estimate_pi()
print "pi is approximately = ", format(pie, '.15f')





# How many iterations does it take to converge?
# ==> 3
