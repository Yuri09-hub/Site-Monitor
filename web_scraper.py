import requests
from notification import message

def Value(link):

    req = requests.get(link)
    return req.status_code

price = None

def Alert(email1,link):
    global price

    new_value = Value(link)
    try:
        if price != new_value:
            price = new_value
            message(email1, price)
    except ConnectionError as e:
        print('Error:',e)






