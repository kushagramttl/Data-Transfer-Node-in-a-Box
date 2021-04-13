import requests
import json


class PortalClient:

    def login(self, url, userName, userPassword):
        session = requests.Session()

        response = session.get(url + "?username=" + userName + "&password=" + userPassword)
        print("Login Response Text : ", response.text)
        if ("Login Error! Try again!" in response.text):
            session.close()
            return None
        return session

    def post_register_container(self, url, session, access_key, secret_key):
        json_object = {
            "access_key": access_key,
            "secret_key": secret_key,
            "port": "9000",
            "ip_address": "localhoast:8000"
        }

        header = {"Content-type": "application/json"}
        response = session.post(url, data=json.dumps(json_object), headers=header)
        print("Register Response : ", response.status_code)
        if response.status_code > 400:
            print("Issue while registering container (container might already be registered)")
        else:
            print("Registration Successful")

    def get_commands(self, url, session):
        respose = session.get(url)
        print("Get command response : ", respose)
        if respose != None:
            commands = respose.json()
            print("Get command JSON data : ", commands)
            return commands
        return {}

    def __init__(self):
        print("Client initiated!")
