import requests
import json


class PortalClient_transfer:
    def get_transfer_list(self, url, session):
        response = session.get(url)
        print("Get transfers response : ", respose)
        if response != None:
            transfers = respose.json()
            print("Get transfers : ", transfers)
            return transfers
        return {}

    def post_transfer(self, url, transferId, session):
        transfer_object = {
            "file_name" : "",
            "bytes_transferred": "0",
            "speed": "0",
            "average_speed": "0",
            "eta": "0",
            "percentage": "0",
            "file_size": "0",
            "stopped": "false"
        }
        json_object = json.dumps(transfer_object)
        header = {"Content-type": "application/json"}
        response = session.post(url + "/" + transferId, data=json.dumps(json_object), headers=header)
        print("Transfer Response : ", response)

    def update_status(self, url, transferId, session, status_obj):
        status = false
        if( int(status_obj.percentage) == 100 ) status = true
        transfer_object = {
            "file_name" : status_obj.name,
            "bytes_transferred": status_obj.bytes,
            "speed": status_obj.speed,
            "average_speed": status_obj.speedAvg,
            "eta": status_obj.eta,
            "percentage": status_obj.percentage,
            "file_size": status_obj.size,
            "stopped": status
        }
        json_object = json.dumps(transfer_object)
        header = {"Content-type": "application/json"}
        response = session.put(url + "/" + transferId, data=json_object, headers=header)

    def __init__(self):
        print("Client initiated!")
