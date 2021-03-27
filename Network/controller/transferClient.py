import requests

def transfer_list(url, session) :
    respose = session.get(url)
    print("Get transfer response : ", respose)
    if respose != None:
        transfers = respose.json()
        print("Get transfer : ", transfers)
        return transfers
    return {}

def post_transfer(url, session) :
    transfer_object = {
        "status" : "Start",
    }
    header = {"Content-type": "application/x-www-form-urlencoded"}
    response = session.put(url, data = transfer_object, headers=header) 
    print("Transfer Response : ", response)
    
    
def update_status(url, session) :
    transfer_object = {
        "status" : "In Progress",
    }    
    header = {"Content-type": "application/x-www-form-urlencoded"}
    response = session.put(url, data = transfer_object, headers=header)    