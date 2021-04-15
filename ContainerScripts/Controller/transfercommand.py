import multiprocessing
from rclone_initiate import make_alias, make_bucket
from protalClient_transfer import PortalClient_transfer
from config import ConfigSingleton
import uuid
from transfer_with_status_back import init_transfer, get_status

"""
The method is the point where transfer of files from th sender to the receiver is managed.
It calls the methods that start, get 
"""


def initiate_transfer(command_obj):
    try:
        print("Inside Transfer Command. New process started")
        print("Command received: ", command_obj)
        print("The processing id is: ", multiprocessing.current_process())

        command = command_obj['command']
        session = command_obj['session']

        # Bucket name
        bucket_name = 'data'

        # Alias name
        alias_name = 'receiver'

        # Create a uuid over here
        make_alias(command['fields']['ip_address'], '9000', alias_name, command['fields']['access_key'],
                   command['fields']['secret_key'])
        make_bucket('receiver', bucket_name)

        # Code from network
        transfer_id = str(uuid.uuid4())

        transfer_client = PortalClient_transfer()

        transfer_init = init_transfer('data', command['fields']['file_name'], alias_name, bucket_name, transfer_id)

        transfer_client.post_transfer(ConfigSingleton.getInstance().config_dict["INIT_TRANSFER_URL"], transfer_id,
                                      session, transfer_init.name)

    except Exception as e:
        print(e)

# while (True):
#     get_status(transfer_id)

# transfers = transfer_client.get_transfer_list(
#     ConfigSingleton.getInstance().config_dict["GET_TRANSFER_LIST_URL"], session)
#
# update_transfer = transfer_client.update_status(
#     ConfigSingleton.getInstance().config_dict["GET_TRANSFER_STATUS_URL"], transfer_id, session)
