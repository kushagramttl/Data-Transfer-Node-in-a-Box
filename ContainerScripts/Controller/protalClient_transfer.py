import requests
import json


class PortalClient_transfer:
    def get_transfer_list(self, url, session):
        respose = session.get(url)
        print("Get transfers response : ", respose)
        if respose != None:
            transfers = respose.json()
            print("Get transfers : ", transfers)
            return transfers
        return {}

    def post_transfer(self, url, transferId, session):
        transfer_object = {
            "status": "Start",
        }
        json_object = json.dumps(transfer_object)
        header = {"Content-type": "application/json"}
        response = session.post(url + "/" + transferId, data=json.dumps(json_object), headers=header)
        print("Transfer Response : ", response)

    def update_status(self, url, transferId, session):
        transfer_object = {
            "status": "In Progress",
        }
        json_object = json.dumps(transfer_object)
        header = {"Content-type": "application/json"}
        response = session.put(url + "/" + transferId, data=json_object, headers=header)

    def __init__(self):
        print("Client initiated!")
