import time
from transferClient import transfer_list, post_transfer, update_status
from config import ConfigSingleton
from ContainerScripts.Controller.portalclient import login

def initiate():

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
    post_transfer( start_transfer, session )


if __name__ == '__main__':
    initiate()
