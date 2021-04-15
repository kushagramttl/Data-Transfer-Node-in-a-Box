import time
from portalclient import PortalClient
from config import ConfigSingleton
from transfercommand import initiate_transfer
from multiprocessing import Process, Pool


def initiate():
    portal_client = PortalClient()

    ConfigSingleton.getInstance().set_config_values()
    wait_time = ConfigSingleton.getInstance().config_dict["WAIT_TIME"]

    # to login into the container
    login_url = ConfigSingleton.getInstance().config_dict["LOGIN_URL"]

    username = input("Please enter your username: ")
    pwd = input("Please enter your password: ")

    session = portal_client.login(login_url, username, pwd)

    if session is not None:

        # for registration of container with portal
        container_registration = ConfigSingleton.getInstance().config_dict["CONTAINER_REGISTER_URL"]

        access_key = input("Please enter your access key: ")
        secret_key = input("Please enter your secret key: ")
        # access_key = "test3"
        # secret_key = "test3"
        portal_client.post_register_container(container_registration, session, access_key, secret_key)

        while True:
            commands = portal_client.get_commands(ConfigSingleton.getInstance().config_dict["FETCH_COMMAND_URL"],
                                                  session)
            if len(commands) > 0:
                print("In main : ", commands)
                # for(command in commands):

                # if command["command"] == "START":
                # p = Process(target=initiate_transfer)
                # p.start()
                # p.join()
                number_of_processes = len(commands)

                command_objects = [{'session': session, 'command': x} for x in commands]

                with Pool(number_of_processes) as p:
                    results = p.map(initiate_transfer, command_objects)
                    print(results)

            time.sleep(wait_time)

            break


# main()

if __name__ == '__main__':
    initiate()
