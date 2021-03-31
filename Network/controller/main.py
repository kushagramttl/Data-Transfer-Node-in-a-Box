import time
from transferClient import get_transfer_list, post_transfer, update_status
from config import ConfigSingleton
from ContainerScripts.Controller.portalclient import login
def initiate( session ):

    ConfigSingleton.getInstance().set_config_values()
    wait_time = ConfigSingleton.getInstance().config_dict["WAIT_TIME"]

    # to login into the container
    login_url = ConfigSingleton.getInstance().config_dict["LOGIN_URL"]

    # username = input("Please enter your username: ")
    # pwd = input("Please enter your password: ")
    username = "admin"
    pwd = "admin"

    session = login(login_url, username, pwd)

    # to start a new transfer
    start_transfer = ConfigSingleton.getInstance().config_dict["INIT_TRANSFER_URL"]
    post_transfer( start_transfer, session , transferId)

    transfers = get_transfer_list(ConfigSingleton.getInstance().config_dict["GET_TRANSFER_LIST_URL"], session)

    update_transfer = update_status( ConfigSingleton.getInstance().config_dict["GET_TRANSFER_STATUS_URL"], session, transferId )

if __name__ == '__main__':
    initiate()
