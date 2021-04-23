import requests
import json
import sys

session = requests.Session()


def add_local():
    print('Inside add local')

    params = {
        "name": "disk",
        "type": "local",
        "parameters": {}
    }

    header = {
        "Content-type": "application/json"
    }
    params_json = json.dumps(params)
    url = "http://rclone:5572/config/create"
    response = session.post(url, data=params_json, headers=header)
    print(response)
    print(response.text)


def make_alias(endpoint, port, alias_name, access_key, secret_key):
    print('Inside make alias')
    # map = {
    #     "access_key_id": access_key,
    #     "secret_access_key": secret_key,
    #     "region": "us-east-1",
    #     "endpoint": endpoint + ":" + port
    # }
    # map_json = json.dumps(map)
    params = {
        "name": alias_name,
        "type": "s3",
        "parameters": {
            "access_key_id": access_key,
            "secret_access_key": secret_key,
            "region": "us-east-1",
            "endpoint": "http://" + endpoint + ":" + port
        }
    }

    header = {
        "Content-type": "application/json"
    }

    print("Parameters for creating alias are: ", params)

    params_json = json.dumps(params)
    url = "http://rclone:5572/config/create"
    response = session.post(url, data=params_json, headers=header)
    print(response)
    print(response.text)


# remote_dir here should contain alias to that endpoint and the bucket to put this file to.
# ie, alias:bucket
def init_transfer(local_dir, file_to_send, remote_alias, remote_bucket, transfer_id):
    # hard_code params
    """
    dummy_params_fortest = {
        "srcFs": "disk:/Users/usr/Desktop",
        "srcRemote": "forPythonTest.txt",
        "dstFs": "test:fortest",
        "dstRemote":"fortest.txt",
        "_async": "true",
        "_group": "job/14"
    }
    """
    params = {
        "srcFs": "disk:/root/data",
        "srcRemote": file_to_send,
        "dstFs": remote_alias + ":" + remote_bucket,
        "dstRemote": file_to_send,
        "_async": "true",
        "_group": transfer_id,
    }
    header = {
        "Content-type": "application/json"
    }
    json_object = json.dumps(params)

    print("parameters for sending file are: ", params)

    url = "http://rclone:5572/operations/copyfile"
    response = session.post(url, data=json_object, headers=header)
    return_obj = {
        "bytes": "0",
        "eta": "0",
        "name": file_to_send,
        "percentage": "0",
        "speed": "0",
        "speedAvg": "0",
        "size": "0"
    }
    print(response)
    print(response.text)
    print(response.json())
    return return_obj


'''
"bytes": total transferred bytes for this file,
"eta": estimated time in seconds until file transfer completion
"name": name of the file,
"percentage": progress of the file transfer in percent,
"speed": average speed over the whole transfer in bytes/sec,
"speedAvg": current speed in bytes/sec as an exponentially weighted moving average,
"size": size of the file in bytes
'''


def get_status(transferId):
    '''
    dummy_params_fortest = {
        "groupid": "job/14"
    }
    '''
    param = {
        "groupid": transferId,
    }
    json_object = json.dumps(param)
    header = {"Content-type": "application/json"}
    url = "http://rclone:5572/core/stats"
    response = session.post(url, data=json_object, headers=header)
    response_json = response.json()

    print("Response json: ", response_json)

    # transfer has already completed.
    if 'transferring' not in response_json or len(response_json['transferring']) == 0:
        transferring = {
            "eta": "0",
            "percentage": "100",
            "speed": "0",
            "name": "",
            "bytes": "0",
            "size": "0",
            "speedAvg": "0"
        }
        return transferring
    else:
        transferring = response_json['transferring'][0]

        if transferring["eta"] is None:
            transferring["eta"] = sys.maxsize

        return transferring
