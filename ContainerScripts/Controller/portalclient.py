import requests
import json

"""
A client class responsible for connecting with portal for commands and login.
"""


class PortalClient:

    def login(self, url, userName, userPassword):
        session = requests.Session()

        response = session.get(url + "?username=" + userName + "&password=" + userPassword)
        print("Login Response Text : ", response.text)
        if "Login Error! Try again!" in response.text:
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
        if respose != None:
            commands = respose.json()
            return commands
        return {}

    def delete_command(self, url, comamnd_id, session):
        delete_url = url + str(comamnd_id)
        response = session.delete(delete_url)
        print(response.text)

        return response

    def __init__(self):
        print("Client class initiated for portal communication")
