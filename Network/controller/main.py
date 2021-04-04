from protalClient_transfer import PortalClient_transfer
from config import ConfigSingleton
from ContainerScripts.Controller.portalclient import login
def initiate():
	ConfigSingleton.getInstance().set_config_values()
    # to start a new transfer
    start_transfer = ConfigSingleton.getInstance().config_dict["INIT_TRANSFER_URL"]

    PortalClient_transfer.post_transfer( start_transfer, transferId)

    transfers = PortalClient_transfer.get_transfer_list(ConfigSingleton.getInstance().config_dict["GET_TRANSFER_LIST_URL"])

    update_transfer = PortalClient_transfer.update_status( ConfigSingleton.getInstance().config_dict["GET_TRANSFER_STATUS_URL"], transferId )

if __name__ == '__main__':
    initiate()
