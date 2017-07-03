# Name: Beshoy Megalaa
# UCID/Email: Bm297@njit.edu
# Course: CS341-452 eLearning
# Assignment: Project 1

# Global variable used to indicate the state
state = None 

# R = {a,b,c,...,z} as set of lower-case Roman letters
#l = {w}

# Checks for www.
def q1(URL, URL_length, i):
	if URL_length != 0 and URL[i] == 'w':
		print("q1: {}".format(URL[i]))
		URL_length -= 1
		i += 1
		if URL_length != 0 and URL[i] == 'w':
			print("q2: {}".format(URL[i]))
			URL_length -= 1
			i += 1
			if URL_length != 0 and URL[i] == 'w':
				print("q3: {}".format(URL[i]))
				URL_length -= 1
				i += 1
				if URL_length != 0 and URL[i] == '.':
					print("q4: {}".format(URL[i]))
					URL_length -= 1
					i += 1
					q5(URL, URL_length,i)
	elif URL_length != 0:
		q5(URL, URL_length,i)

# Checks for R Recursively and acceptance state
def q5(URL, URL_length, i):
	R = "abcdefghijklmnopsqrtxyz"		
	if URL[i] in R:
		print("q5: {}".format(URL[i]))
		URL_length -= 1
		i += 1
		# URL[x] = all lower-case Roman letters
		while(URL_length != 0 and URL[i] != '.'):
			print("q5: {}".format(URL[i]))
			URL_length -= 1
			i += 1
		# If last letter than it's in accepted state
		if(URL_length == 0):
			global state
			state = "Accepted!"
		else:
			q6(URL, URL_length, i)

# Checks for dot
def q6(URL, URL_length, i):
	if URL[i] == '.':
		print("q6: {}".format(URL[i]))
		URL_length -= 1
		i += 1
		if URL_length != 0:
			q7(URL, URL_length, i)

# Checks for c
def q7(URL, URL_length, i):
	if URL[i] == 'c':
		print("q7: {}".format(URL[i]))
		URL_length -= 1
		i += 1
		if URL_length != 0:
			if URL[i] == 'a':
				q8(URL, URL_length, i)
			else:
				q9(URL, URL_length, i)

# Checks for a and accpetance state
def q8(URL, URL_length, i):
	if URL[i] == 'a':
		print("q7: {}".format(URL[i]))
		URL_length -= 1
		i += 1
		# If last letter than it's in accepted state
		if(URL_length == 0):
			global state
			state = "Accepted!"

# Checks for o
def q9(URL, URL_length, i):
	if URL[i] == 'o':
		print("q9: {}".format(URL[i]))
		URL_length -= 1
		i += 1
		if URL_length != 0 and URL[i] == '.':
			q6(URL, URL_length, i)
		elif URL_length != 0:
			q10(URL, URL_length, i)

# Checks for m and acceptance state
def q10(URL, URL_length, i):
	if URL[i] == 'm':
		print("q10: {}".format(URL[i]))
		URL_length -= 1
		i += 1
		if(URL_length == 0):
			global state
			state = "Accepted!"

def main():
	
	while True:
		string = input("Would you like to enter URL to check? (y/n)  ")
		if(string.lower() == 'n'):
			break
		else:
			URL = input("Enter the URL: ")
			i = 0 # index
			URL_length = len(URL)
			global state
			state = "Rejected!"
			q1(URL, URL_length, i)
			print("URL {}".format(state))

if __name__ == "__main__":
	main()