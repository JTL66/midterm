#Midterm
#some imports
import re
import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #this help to lift the certification for that https
api_endpoint = "https://api.exchangerate-api.com/v4/latest/"

#decorator
def loggable(func):         
    def inner(arg1,arg2,arg3): #here are three parameters
        s = func(arg1,arg2,arg3)
        with open("log.txt", "a") as log_file:
            log_file.write("Input:{}\n".format(arg1,arg2,arg3))
            log_file.write("Output:{}\n".format(s))
        return s
    return inner #return the decorator function


def page_exists(page): #test if the api endpoint exits
    try:
        urllib.request.urlopen(page)
        return True
    except:
        return False

@loggable
def currency_converter(amount,FROM,TO): 

    if (page_exists(api_endpoint + FROM)): 
        page = urllib.request.urlopen(api_endpoint + FROM) #request api_endpoint+FROM website
        content = page.read().decode("utf-8") #keep in mind the byte string needs to be decoded
        data = json.loads(content) #parse the json into python dictionary
        rates = data["rates"] # get rates list from the data dict
        if TO in rates:
            rate = rates[TO]  # get the accurate rate from the rates list
        else:
            return "TO currency code not found"
        if not rates:
            return "rates not found"
    else:
        print("ERROR:invalid API endpoint")
        return "one or more currency codes not found"
    return "{} in {} = {} in {}".format(amount, FROM, amount * rate, TO)  #get the format result


def main():
    while (True):
    	# if one of the inputs is not valid, the program should not collect the remaining inputs
    	# and should go back to collecting the inputs from the beginning
        try: 
            amount = input("Enter amount to be converted(q to quit): ")
            if amount == 'q' or amount == 'Q':
                print("Exiting")
                break
            amount = float(amount)
        except ValueError:
             print("amount enter wrong")
             continue

        FROM = input("Enter FROM currency 3 letter code: ")
        if not FROM.isupper():
            print("FROM enter wrong")
            continue

        TO = input("Enter TO currency 3 letter code:")
        if not TO.isupper():
            print("TO enter wrong")
            continue
        print(currency_converter(amount,FROM,TO))
        print("\n")


if __name__ == '__main__':
    main()


