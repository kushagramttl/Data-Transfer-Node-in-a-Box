import requests
import json
import threading
# remote_dir here should contain alias to that endpoint and the bucket to put this file to.
# ie, alias:bucket
def init_transfer(local_dir, file_to_send, remote_dir, transferId) :
    # hard_code params
    '''
    dummy_params_fortest = {
        "srcFs": "disk:/Users/susu/Desktop",
        "srcRemote": "forPyhonTestee.txt",
        "dstFs": "test:fortest",
        "dstRemote":"fortest.txt",
        "_async": "true",
        "group": "job/14"
    }
    '''
    params = {
        "srcFs": local_dir,
        "srcRemote": file_to_send,
        "dstFs": remote_dir,
        "dstRemote": file_to_send,
        "_async": "true",
        "group": transferId
    }
    session = requests.Session()
    header = {
        "Content-type": "application/json"
    }
    json_object = json.dumps(params)

    url = "http://localhost:5572/operations/copyfile"
    response=session.post( url, data=json_object, headers=header)
    return_obj={
        "bytes":"0",
        "eta":"0",
        "name":file_to_send,
        "percentage":"0",
        "speed":"0",
        "speedAvg":"0",
        "size":"0"
    }
    return_json=json.dumps(return_obj)
    print(response.json())
    print(return_json)
    return return_json

'''
"bytes": total transferred bytes for this file,
"eta": estimated time in seconds until file transfer completion
"name": name of the file,
"percentage": progress of the file transfer in percent,
"speed": average speed over the whole transfer in bytes/sec,
"speedAvg": current speed in bytes/sec as an exponentially weighted moving average,
"size": size of the file in bytes
'''
def get_status_helper( transferId ) :
    '''
    dummy_params_fortest = {
        "group": "job/14"
    }
    '''
    param = {
        "group": transferId,
    }
    json_object = json.dumps(param)
    session = requests.Session()
    header = {"Content-type": "application/json"}
    url = "http://localhost:5572/core/stats"
    response = session.post( url, data=json_object, headers=header)
    response_json = response.json()
    # transfer has already completed.
    if response_json['transfers'] == 0 :
        transferring = {
            "eta":"0",
            "percentage":"100",
            "speed": "0",
            "name" : "",
            "bytes" : "0",
            "size" : "0",
            "speedAvg" : "0"
        }
        transferring_object = json.dumps(transferring)
        print( "transferring" ,  transferring_object)
        return transferring
    else :
        transferring = response_json['transferring'][0]
        print( "transferring" ,  transferring)
        return transferring

def get_status( transferId ):
  threading.Timer(5.0, get_status_helper).start()
  print "Hi there!"
