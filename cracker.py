import requests
import getpass

password = getpass.getpass("Enter Your Password Here: ")

SUCCESS_URL = "https://run.mocky.io/v3/f15ac584-9adc-47d4-9b81-43a11baebc87"
FAILURE_URL = "https://run.mocky.io/v3/b22584c7-d0e2-46f7-bc1a-140e73c8645b"

response = requests.get(SUCCESS_URL)
response1 = requests.get(FAILURE_URL)



with open('0to1000.txt', 'r') as file:
    for line in file:
        new=int(line.strip())
        if password == str(new):
            print(response.json())
            print("Cracked Password is", new)
            break
    else:
        print(response1.json())
        print("Your password isn't in this list")
    




