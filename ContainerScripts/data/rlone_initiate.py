import subprocess

def make_alias(endpoint, port, alias_name, access_key, secret_key):
  endp = "http://" + endpoint + ":" + port
  make_alias_cmd = "rclone config create " + alias_name + " s3 env_auth true access_key_id "+ access_key + " secret_access_key " + secret_key+ " region us-east-1 endpoint " + endp
  subprocess.run( make_alias_cmd , shell=True)

def make_bucket( alias_name, bucket_name) :
  make_bucket_cmd="rclone mkdir " + alias_name + ":" + bucket_name
  subprocess.run( make_bucket_cmd , shell=True)

def init_transfer( local_dir,  alias_name, bucket_name ):
  start_transfer_cmd = "rclone copy " + local_dir + " " + alias_name + ":" + "bucket_name"
  subprocess.run( start_transfer_cmd , shell=True)
