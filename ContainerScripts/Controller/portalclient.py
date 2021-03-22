import requests
import json

def login(url, userName, userPassword):
    session = requests.Session()

    response = session.get(url + "?username=" + userName + "&password=" + userPassword)
    print("Login Response : " , response.text)
    return session

def post_register_container(url, session):
    json_object = {
        "access_key" : "test6",
        "secret_key" : "test6",
        "port": "9000",
        "ip_address": "localhoast:8000"
    }

    header = {"Content-type": "application/x-www-form-urlencoded"}
    response = session.post(url, data=json_object, headers= header)
    print("Register Response : " , response)
    # print(response.text)

def get_commands(url, session):
    respose = session.get(url)
    print("Get command response : " , respose)
    commands = respose.json()
    print("Get command JSON data : " , commands)
    return commands
