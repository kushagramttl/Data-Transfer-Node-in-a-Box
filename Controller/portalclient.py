import requests
import json

def get_commands(url):
    respose = requests.get(url)
    print(respose)
    json_data = respose.json()
    print(json_data)
    
    return json_data