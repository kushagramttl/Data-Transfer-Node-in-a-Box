import multiprocessing
from protalClient_transfer import PortalClient_transfer
from config import ConfigSingleton
import uuid
from transfer_with_status_back import init_transfer, get_status, make_alias
import config
import time
from portalclient import PortalClient

"""
The method is the point where transfer of files from th sender to the receiver is managed.
It calls the methods that start transfer, get transfer status, delete command on portal and update status of transfer
"""


def initiate_transfer(command_obj):
    try:
        print("Inside Transfer Command. New process started")
        print("Command received: ", command_obj)
        print("The processing id is: ", multiprocessing.current_process())

        portalclient = PortalClient()

        command = command_obj['command']
        session = command_obj['session']

        print(command)
        command_id = command["fields"]["command_id"]

        # Bucket name
        bucket_name = 'data'

        # Alias name
        alias_name = 'receiver'

        make_alias(command['fields']['ip_address'], '9000', alias_name, command['fields']['access_key'],
                   command['fields']['secret_key'])

        # Create a transfer id that can be updated on portal
        transfer_id = str(uuid.uuid4())

        status_wait = config.ConfigSingleton.config_dict["GET_STATUS_TIME"]

        transfer_client = PortalClient_transfer()

        transfer_init = init_transfer(command['fields']['file_name'], alias_name, bucket_name, transfer_id)

        transfer_client.post_transfer(ConfigSingleton.getInstance().config_dict["INIT_TRANSFER_URL"], transfer_id,
                                      session, transfer_init['name'])

        portalclient.delete_command(ConfigSingleton.getInstance().config_dict["DELETE_COMMAND_URL"], command_id,
                                    session)

        while True:
            status = get_status(transfer_id)

            print("The status of Transfer from RClone: ", status)

            transfer_client.update_status(ConfigSingleton.getInstance().config_dict["INIT_TRANSFER_URL"], transfer_id,
                                          session, status)

            time.sleep(status_wait)

            if status["percentage"] == 100 or status["percentage"] == "100":
                break

    except Exception as e:
        print(e)
