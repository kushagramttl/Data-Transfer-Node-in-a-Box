import urllib.request, json 
import subprocess

def pull_json() :
  
  url_address ='https://api.twitter.com/1.1/statuses/user_timeline.json'
  with urllib.request.urlopen(url_address) as url:
      data = json.loads(url.read().decode())
      print(data) 
  return data

#dummy json object
a ={"endpoint":"192.168.0.33:9000", 
   "name": "BobMachine", 
    "access":"testKey2",
    "secret":"testsecret2",
    "local directory" : "/Users/susu/Desktop/newtest.txt"
    }

# conversion to JSON done by dumps() function 
json_string = json.dumps(a) 

#The JSON module can also take a JSON string and convert it back to a dictionary structure:
datastore = json.loads(json_string)
# printing the output


def make_alias():
  endp = "http://" + datastore["endpoint"]
  make_alias_cmd = "mc config host add " + datastore["name"] + " " + endp + " " + datastore["access"] + " " + datastore["secret"] + " --api S3v4"
  subprocess.run( make_alias_cmd , shell=True)

def create_bucket( alias,  bucket_name ) :
  create_bucket_cmd = "mc mb " + alias + "/" + bucket_name 
  subprocess.run( create_bucket_cmd  , shell=True)
  
def start_transfer():
  start_transfer_cmd = "mc cp " + datastore["local directory"] + " " + datastore["name"] + "/receive"
  subprocess.run( start_transfer_cmd , shell=True)
  