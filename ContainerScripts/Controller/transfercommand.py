import multiprocessing
from rclone_initiate import make_alias, init_transfer, make_bucket

def initiate_transfer(command):
    print("Inside Transfer Command. New process started")
    print("Command received: ", command)
    print("The processing id is: ", multiprocessing.current_process())

    # Create a uuid over here
    make_alias('128.31.25.199', '9000', 'receiver', 'minio', 'minio123')
    make_bucket('receiver', 'data')
    init_transfer('data/foo.txt', 'receiver', 'data')
