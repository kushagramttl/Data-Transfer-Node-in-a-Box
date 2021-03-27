import multiprocessing


def initiate_transfer(command):
    print("Inside Transfer Command. New process started")
    print("Command received: ", command)
    print("The processing id is: ", multiprocessing.current_process())