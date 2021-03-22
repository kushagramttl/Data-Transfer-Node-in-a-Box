from paramiko import SSHClient
from scp import SCPClient
from paramiko import AutoAddPolicy

ssh = SSHClient()
ssh.set_missing_host_key_policy( AutoAddPolicy())
ssh.connect(hostname = '', username = '', password = '', port = )

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
scp.put('from', recursive=True, remote_path='to')

scp.close()
