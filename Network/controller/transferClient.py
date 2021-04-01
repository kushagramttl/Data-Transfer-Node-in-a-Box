import requests

def get_transfer_list(url) :
    session = requests.Session()
    respose = session.get(url)
    print("Get transfer response : ", respose)
    if respose != None:
        transfers = respose.json()
        print("Get transfer : ", transfers)
        return transfers
    return {}

def post_transfer(url, transferId) :
    transfer_object = {
        "status" : "Start",
    }
    session = requests.Session()
    header = {"Content-type": "application/x-www-form-urlencoded"}
    response = session.post(url + "/" + transferId, data = transfer_object, headers=header)
    print("Transfer Response : ", response)

def update_status(url, transferId) :
    transfer_object = {
        "status" : "In Progress",
    }
    session = requests.Session()
    header = {"Content-type": "application/x-www-form-urlencoded"}
    response = session.put(url + "/" + transferId, data = transfer_object, headers=header)
