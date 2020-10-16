#Program1

#start with the user input and validation
user_input = input("Enter zip code(q to quit):")
print(user_input) 


#Validate the input
import re

user_input = input("Enter zip code(q to quit):")
#beginning of the string and end of the string pattern is important
#so is adding meaningful comments
regexp = re.compile("^\d{5}$")
if not regexp.search(user_input):
	print("Invalid input {}".format(user_input))



#adding looping logic:
import re

#takes a zipcode string as a parameter
#returns location string
def zipcode_lookup(zipcode):
    while(True):
        user_input = input("Enter zip code(q to quit):")
        if(user_input == 'q' or user_input == 'Q'):
            print("Exiting")
            break
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
        regexp = re.compile("^\d{5}$")
        if not regexp.search(user_input):
            print("Invalid input {}".format(user_input))

zipcode_lookup("")


#Adding zip code lookup function
import re

#takes a zipcode string as a parameter
#returns location string
def zipcode_lookup(zipcode):
	return "echo:"+zipcode

while(True):
	user_input = input("Enter zip code(q to quit):")
	if(user_input == 'q' or user_input == 'Q'):
		print("Exiting")
		break
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
	regexp = re.compile("^\d{5}$")
	if not regexp.search(user_input):
		print("Invalid input {}".format(user_input))
	else:
		print(zipcode_lookup(user_input))

#adding a real zip code lookup

import re
import urllib.request
import json


api_endpoint = "http://api.zippopotam.us/us/"

def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False

#takes a zipcode string as a parameter
#returns location string
def zipcode_lookup(zipcode):
	if(page_exists(api_endpoint+zipcode)):
		page = urllib.request.urlopen(api_endpoint+zipcode)
		print(page.read())
	else:
		print("ERROR:invalid API endpoint")
	return "echo:"+zipcode

while(True):
	user_input = input("Enter zip code(q to quit):")
	if(user_input == 'q' or user_input == 'Q'):
		print("Exiting")
		break
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
	regexp = re.compile("^\d{5}$")
	if not regexp.search(user_input):
		print("Invalid input {}".format(user_input))
	else:
		print(zipcode_lookup(user_input))


#if I change the URL in the code to
#api_endpoint = "https://api.zippopotam.usa/us/"


#Given the requirement #7, we need the only first element from the "places"

import re
import urllib.request
import json


api_endpoint = "http://api.zippopotam.us/us/"

def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False

#takes a zipcode string as a parameter
#returns location string
def zipcode_lookup(zipcode):
	if(page_exists(api_endpoint+zipcode)):
		page = urllib.request.urlopen(api_endpoint+zipcode)
		content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded
		data = json.loads(content)
		place = data["places"][0] #[0] from requirement 7
		print("{}:{}, {}".format(zipcode, place["place name"], place["state abbreviation"]))
	else:
		print("ERROR:invalid API endpoint")
	return "echo:"+zipcode

while(True):
	user_input = input("Enter zip code(q to quit):")
	if(user_input == 'q' or user_input == 'Q'):
		print("Exiting")
		break
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
	regexp = re.compile("^\d{5}$")
	if not regexp.search(user_input):
		print("Invalid input {}".format(user_input))
	else:
		print(zipcode_lookup(user_input))


#And now, return it from the function:

import re
import urllib.request
import json


api_endpoint = "http://api.zippopotam.us/us/"

def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False

#takes a zipcode string as a parameter
#returns location string
def zipcode_lookup(zipcode):
	if(page_exists(api_endpoint+zipcode)):
		page = urllib.request.urlopen(api_endpoint+zipcode)
		content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded
		data = json.loads(content)
		place = data["places"][0] #[0] from requirement 7
	else:
		print("ERROR:invalid API endpoint")
	return "{}:{}, {}".format(zipcode, place["place name"], place["state abbreviation"])

while(True):
	user_input = input("Enter zip code(q to quit):")
	if(user_input == 'q' or user_input == 'Q'):
		print("Exiting")
		break
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
	regexp = re.compile("^\d{5}$")
	if not regexp.search(user_input):
		print("Invalid input {}".format(user_input))
	else:
		print(zipcode_lookup(user_input))


# what if we put 00000 (requirement #2)?
# errors
# how to handle that

import re
import urllib.request
import json


api_endpoint = "http://api.zippopotam.us/us/"

def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False

#takes a zipcode string as a parameter
#returns location string
def zipcode_lookup(zipcode):
	if(page_exists(api_endpoint+zipcode)):
		page = urllib.request.urlopen(api_endpoint+zipcode)
		content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded
		data = json.loads(content)
		if not data:
			return "place not found"
		place = data["places"][0] #[0] from requirement 7
		if not place:
			return "place not found"
	else:
		print("ERROR:invalid API endpoint")
		return "place not found"
	return "{}:{}, {}".format(zipcode, place["place name"], place["state abbreviation"])

while(True):
	user_input = input("Enter zip code(q to quit):")
	if(user_input == 'q' or user_input == 'Q'):
		print("Exiting")
		break
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
	regexp = re.compile("^\d{5}$")
	if not regexp.search(user_input):
		print("Invalid input {}".format(user_input))
	else:
		print(zipcode_lookup(user_input))


# user input validation should logically be inside zipcode lookup function 
# in the form of argument validation


import re
import urllib.request
import json


api_endpoint = "http://api.zippopotam.us/us/"

def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False

#takes a zipcode string as a parameter
#returns location string
def zipcode_lookup(zipcode):
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
	regexp = re.compile("^\d{5}$")
	if not regexp.search(zipcode):
		return "Invalid input {}".format(zipcode)
	
	if(page_exists(api_endpoint+zipcode)):
		page = urllib.request.urlopen(api_endpoint+zipcode)
		content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded
		data = json.loads(content)
		if not data:
			return "place not found"
		place = data["places"][0] #[0] from requirement 7
		if not place:
			return "place not found"
	else:
		print("ERROR:invalid API endpoint")
		return "place not found"
	return "{}:{}, {}".format(zipcode, place["place name"], place["state abbreviation"])

while(True):
	user_input = input("Enter zip code(q to quit):")
	if(user_input == 'q' or user_input == 'Q'):
		print("Exiting")
		break
	print(zipcode_lookup(user_input))


#Pytest




#Extra 

#Create a decorator function, and decorate the zipcode lookup function
#The decorator function should log every function call with input and output into a log.txt file
import re
import urllib.request
import json

api_endpoint = "http://api.zippopotam.us/us/"

def loggable(func):
	def inner(arg):
		s = func(arg)
		with open("log.txt", "a") as log_file:
			log_file.write("Input:{}\n".format(arg))
			log_file.write("Output:{}\n".format(s))
		return s
	return inner #return the decorator function


def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False

#takes a zipcode string as a parameter
#returns location string
@loggable
def zipcode_lookup(zipcode):
	#beginning of the string and end of the string pattern is important
	#so is adding meaningful comments
	regexp = re.compile(r'^\d{5}$')
	if not regexp.search(zipcode):
		return "Invalid input {}".format(zipcode)
	
	if(page_exists(api_endpoint+zipcode)):
		page = urllib.request.urlopen(api_endpoint+zipcode)
		content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded
		data = json.loads(content)
		if not data:
			return "place not found"
		place = data["places"][0] #[0] from requirement 7
		if not place:
			return "place not found"
	else:
		print("ERROR:invalid API endpoint")
		return "place not found"
	return "{}:{}, {}".format(zipcode, place["place name"], place["state abbreviation"])


def main():
	while(True):
		user_input = input("Enter zip code(q to quit):")
		if(user_input == 'q' or user_input == 'Q'):
			print("Exiting")
			break
		print(zipcode_lookup(user_input))

if __name__ == '__main__':
	main()


