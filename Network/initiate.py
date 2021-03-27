import urllib.request, json 
import subprocess

def make_alias():
  #dummy json object
  a ={"endpoint":"192.168.0.33:9000", 
     "name": "bobMachine", 
      "access":"testKey2",
      "secret":"testsecret2",
      "local directory" : "/Users/susu/Desktop/forPyhonTest.txt"
      }
  
  # conversion to JSON done by dumps() function 
  json_string = json.dumps(a) 
  
  #The JSON module can also take a JSON string and convert it back to a dictionary structure:
  datastore = json.loads(json_string)
  # printing the output
  
  endp = "http://" + datastore["endpoint"]
  make_alias_cmd = "mc config host add " + datastore["name"] + " " + endp + " " + datastore["access"] + " " + datastore["secret"] + " --api S3v4"
  subprocess.run( make_alias_cmd , shell=True)

def create_bucket( alias,  bucket_name ) :
  create_bucket_cmd = "mc mb " + alias + "/" + bucket_name 
  subprocess.run( create_bucket_cmd  , shell=True)
  
def start_transfer():
  #dummy json object
  a ={"endpoint":"192.168.0.33:9000", 
     "name": "bobMachine", 
      "access":"testKey2",
      "secret":"testsecret2",
      "local directory" : "/Users/susu/Desktop/forPyhonTest.txt"
      }
  
  # conversion to JSON done by dumps() function 
  json_string = json.dumps(a) 
  
  #The JSON module can also take a JSON string and convert it back to a dictionary structure:
  datastore = json.loads(json_string)
  # printing the output
  
  start_transfer_cmd = "mc cp " + datastore["local directory"] + " " + datastore["name"] + "/fortest2"
  subprocess.run( start_transfer_cmd , shell=True)
  
def main():
  make_alias()
  create_bucket("bobMachine",  "fortest2")
  start_transfer()
	
if __name__ == '__main__':
    main()