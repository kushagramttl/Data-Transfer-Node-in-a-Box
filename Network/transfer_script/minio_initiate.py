import subprocess

def make_alias(endpoint, alias_name, access_key, secret_key):
  endp = "http://" + endpoint
  make_alias_cmd = "mc config host add " + alias_name + " " + endp + " " + access_key + " " + secret_key + " --api S3v4"
  subprocess.run( make_alias_cmd , shell=True)

def init_transfer( local_dir,  alias_name, bucket_name ):
  start_transfer_cmd = "mc cp " + local_dir + " " + alias_name + "/" + "bucket_name"
  subprocess.run( start_transfer_cmd , shell=True)
