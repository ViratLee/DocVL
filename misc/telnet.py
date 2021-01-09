# telnet program example
import socket, select, string, sys

#main function
if __name__ == "__main__":
    
    if(len(sys.argv) < 3) :
        print('Usage : python telnet.py hostname port')
        sys.exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print(f'Unable to connect {host}. port {port} ')
        sys.exit()
    
    #print('Connected to remote host')
    
    message = f"""
    telnet {host} {port}
    """
    print(message)

    # while 1:
    #   socket_list = [sys.stdin, s]
        
    #   # Get the list sockets which are readable
    #   read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        
    #   for sock in read_sockets:
    #       #incoming message from remote server
    #       if sock == s:
    #           data = sock.recv(4096)
    #           if not data :
    #               print('Connection closed')
    #               sys.exit()
    #           else :
    #               #print(data)
    #               sys.stdout.write(data)
            
    #       #user entered a message
    #       else :
    #           msg = sys.stdin.readline()
    #           s.send(msg)