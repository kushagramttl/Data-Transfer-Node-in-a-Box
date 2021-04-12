import multiprocessing
from rclone_initiate import make_alias, init_transfer, make_bucket
from protalClient_transfer import PortalClient_transfer
from config import ConfigSingleton
import uuid

def initiate_transfer(session, command):
    print("Inside Transfer Command. New process started")
    print("Command received: ", command)
    print("The processing id is: ", multiprocessing.current_process())

    # Create a uuid over here
    make_alias('128.31.25.199', '9000', 'receiver', 'minio', 'minio123')
    make_bucket('receiver', 'data')
    init_transfer('data/foo.txt', 'receiver', 'data')

    # Code from network
    transfer_id = uuid.uuid4()

    transfer_client = PortalClient_transfer()

    transfer_client.post_transfer(ConfigSingleton.getInstance().config_dict["INIT_TRANSFER_URL"], transfer_id,
                                  session)

    transfers = transfer_client.get_transfer_list(
        ConfigSingleton.getInstance().config_dict["GET_TRANSFER_LIST_URL"], session)

    update_transfer = transfer_client.update_status(
        ConfigSingleton.getInstance().config_dict["GET_TRANSFER_STATUS_URL"], transfer_id, session)
