import requests

class PortalClient_transfer:
    def get_transfer_list(url, session) :
        respose = session.get(url)
        print("Get transfers response : ", respose)
        if respose != None:
            transfers = respose.json()
            print("Get transfers : ", transfers)
            return transfers
        return {}

    def post_transfer(url, transferId, session) :
        transfer_object = {
            "status" : "Start",
        }
        header = {"Content-type": "application/json"}
        response = session.post(url + "/" + transferId, data = transfer_object, headers=header)
        print("Transfer Response : ", response)

    def update_status(url, transferId, session) :
        transfer_object = {
            "status" : "In Progress",
        }
        header = {"Content-type": "application/json"}
        response = session.put(url + "/" + transferId, data = transfer_object, headers=header)

    def __init__(self):
        print("Client initiated!")
