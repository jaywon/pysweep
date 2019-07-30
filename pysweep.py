import subprocess
import os

responses = []
network_id = "10.0.2."

def process_list(my_list):
    pass

def write_to_log(my_list):
    pass

def ping():
    #result = subprocess.run(["fping", "10.0.2.10"], capture_output=True, text=True)

    for num in range(1, 256):
        ip_address = network_id + str(num)
        print(ip_address)
#
#    for i in (range(10):
#        print(responses[i])
#
#    for character in "jason":
#        print(character)

    for response in responses:
        print(response)
    

if __name__ == '__main__':
    ping()

