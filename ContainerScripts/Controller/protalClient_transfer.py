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
            "status": "In Progress",
            "file_name" : "",
            "bytes_transferred": "0",
            "speed": "0",
            "average_speed": "0",
            "eta": "48 8",
            "percentage": "0",
            "file_size": "0",
            "stopped": "false"
        }
        json_object = json.dumps(transfer_object)
        header = {"Content-type": "application/json"}
        response = session.post(url + "/" + transferId, data=json.dumps(json_object), headers=header)
        print("Transfer Response : ", response)

    def update_status(self, url, transferId, session):
        transfer_object = {
            "status": "In Progress",
            "file_name" : "",
            "bytes_transferred": "500",
            "speed": "100",
            "average_speed": "80",
            "eta": "48 minutes 6 seconds",
            "percentage": "5",
            "file_size": "100",
            "stopped": "false"
        }
        json_object = json.dumps(transfer_object)
        header = {"Content-type": "application/json"}
        response = session.put(url + "/" + transferId, data=json_object, headers=header)

    def __init__(self):
        print("Client initiated!")
