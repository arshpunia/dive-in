import json 
import requests
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import logging 
import os
from dotenv import load_dotenv

def get_request_token():
    load_dotenv()
    consumer_key = os.getenv('POCKET_API_KEY')
    url = 'https://getpocket.com/v3/oauth/request'
    post_fields = {"consumer_key":{consumer_key},"redirect_uri":"http://www.google.com"}   
    request = Request(url,urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)
    
def get_access_token():
    load_dotenv()
    consumer_key = os.getenv('POCKET_API_KEY')
    request_token = os.getenv('POCKET_REQUEST_TOKEN')
    url = 'https://getpocket.com/v3/oauth/authorize' # Set destination URL here
    post_fields = {"consumer_key":{consumer_key},"code":{request_token}}  # Set POST fields here
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)

def make_get_requests():
    load_dotenv()
    consumer_key = os.getenv('POCKET_API_KEY')
    access_token = os.getenv('POCKET_ACCESS_TOKEN')
    parameters = {"consumer_key":{consumer_key},"access_token":{access_token}}
    response = requests.get("https://getpocket.com/v3/get", params=parameters)
    json_rep = response.json()
    list = json_rep['list']
    count=0
    for header in list:
        count+=1
        print(list[str(header)]['resolved_title'])
    print(str(count))
    
def main():
    make_get_requests()

if __name__=="__main__":
    main()