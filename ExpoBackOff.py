# your code goes here
import requests
import json
import random
import time

def callApi(num_retries):
    chance_of_collision = random.randint(0,5)
    if(num_retries<chance_of_collision):
        raise Exception("Collisions")
    url = "https://fakerapi.it/api/v1/places?_quantity=1"
    response = requests.request("GET", url)
    return response.status_code

def paymentGateway() :

   MAX_RETRIES=5

   num_retries = 0

   while (num_retries <= MAX_RETRIES) :

    try :

         # actual code goes here
        print("Calling payment API")
        status=callApi(num_retries)
        if status == 200:
            return "Success"
        else:
            return "Failed"
        

    except Exception as e :
        print(e)
        print("Retrying .....")
        num_retries = num_retries+1
        if (num_retries > MAX_RETRIES) :
            return "Failed"
        print("Try",num_retries)
        backoff_before_retry(num_retries)

def backoff_before_retry(num_retries) :
	jitter = random.randint(1,999)
	backoff_interval = 2**(num_retries-1)*5 + jitter/1000
	print("Sleeping for :",backoff_interval,"timeUnits")
	time.sleep(backoff_interval/100)


