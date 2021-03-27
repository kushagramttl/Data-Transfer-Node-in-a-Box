import time
from portalclient import get_commands, post_register_container, login
from config import ConfigSingleton
from transfercommand import initiate_transfer
from multiprocessing import Process, Pool
from testminio import main

def initiate():

    ConfigSingleton.getInstance().set_config_values()
    wait_time = ConfigSingleton.getInstance().config_dict["WAIT_TIME"]

    # to login into the container
    login_url = ConfigSingleton.getInstance().config_dict["LOGIN_URL"]

    # username = input("Please enter your username: ")
    # pwd = input("Please enter your password: ")

    username = "alice"
    pwd = "DockerBaba"

    session = login(login_url, username, pwd)

    # for registration of conatiner with portal
    container_registration = ConfigSingleton.getInstance().config_dict["CONTAINER_REGISTER_URL"]

    # access_key = input("Please enter your access key: ")
    # secret_key = input("Please enter your secret key: ")
    access_key = "test3"
    secret_key = "test3"
    post_register_container(container_registration, session, access_key, secret_key)

    while(True):
        commands = get_commands(ConfigSingleton.getInstance().config_dict["FETCH_COMMAND_URL"], session)
        if len(commands) > 0:
            print("In main : ", commands)
        # for(command in commands):

        # if command["command"] == "START":
            # p = Process(target=initiate_transfer)
            # p.start()
            # p.join()
            number_of_processes = len(commands)

            with Pool(number_of_processes) as p:
                results = p.map(initiate_transfer, commands)
                print(results)

        time.sleep(wait_time)

        break

  


    # main()

if __name__ == '__main__':
    initiate()
