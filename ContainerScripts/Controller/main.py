import time
from portalclient import get_commands
from config import ConfigSingleton
from transfercommand import initiate_transfer
from multiprocessing import Process

def initiate():
    ConfigSingleton.getInstance().set_config_values()
    wait_time = ConfigSingleton.getInstance().config_dict["WAIT_TIME"]

    while(True):
        command = get_commands(ConfigSingleton.getInstance().config_dict["PORTAL_URL"])

        if command["command"] == "START":
            p = Process(target=initiate_transfer)
            p.start()
            p.join()

        time.sleep(wait_time)

        break


if __name__ == '__main__':
    initiate()
