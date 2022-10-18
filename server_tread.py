import socket
import os
import konfig
from _thread import *
import threading

# import socketserver
# import http.server

host = '127.0.0.1'
port = 8080
path = 'C:/Users/ASUS/OneDrive/Dokumen/Abdulatif/kuliah/sem9/progjar/WebServer/'
# try:
    # newdir = os.path.dirname(path)
    # print('direktori diganti')
    # print(os.listdir(newdir))
# except:
    # print("ngga terganti")
# Create socket
print_lock = threading.Lock

def threaded(client_connection):
    client_connection, client_address = server_socket.accept()
    while True:
        data = client_connection.recv(1024).decode
        if not data:
            response='HTTP/1.0 404 Not Found\n\n'
            client_connection.send(response.encode)
            # lock released on exit
            print_lock.release()
            break
 
        # reverse the given string from client
        else:
            response = 'HTTP/1.0 200 OK\n\n'
 
        # send back reversed string to client
            client_connection.sendall(response.encode)
 
    # connection closed
    client_connection.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)
print( '%s is Activated ...' % host)
print('Listening on port %s ...' % port)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    
    # Get the client request
    request = client_connection.recv(1024).decode()
    # print(request)
    
    #get filename
    headers = request.split('\n')
    filename = headers[0].split()[1]
    # print('request nya nihh:', filename)
    indexname = filename.replace('/','')
    # print('index name:',indexname,'==')
    hostname = headers[1].split(':')[1]
    print(hostname, ' Terhubung ......')
    koneksi = headers[2].split()[1]
    print('connection: ', koneksi)

    #direktori dan konfigurasi
    if hostname == konfig.hostname1:
        Directory = konfig.Directory1
        newdir = os.path.dirname(Directory)
    elif hostname == konfig.hostname2:
        Directory = konfig.Directory2
        newdir = os.path.dirname(Directory)
    else:
        Directory = konfig.Directory
        newdir = os.path.dirname(Directory)
    
    if filename == '/':
            filename = '/index.html'

            fin = open(Directory + filename)
            content = fin.read()
            fin.close()

            # Send HTTP response
            response = 'HTTP/1.0 200 OK\n\n'+ content
            client_connection.sendall(response.encode())
            client_connection.close()
            # print(os.path)

    elif indexname not in os.listdir(newdir):
                fin = open(Directory + '/404.html')
                content = fin.read()
                fin.close()

                response = 'HTTP/1.0 404 Not Found\n\n' + content
                client_connection.sendall(response.encode())
                client_connection.close()

    elif '.' in filename:        
     # Get the content of htdocs/index.html        
        if 'html' in filename:
            fin = open(Directory + filename)
            content = fin.read()
            fin.close()
            # Send HTTP response
            response = 'HTTP/1.0 200 OK\n\n' + content
            client_connection.sendall(response.encode())
            client_connection.close()

        # elif 'pdf' in filename:
        #     fin = open(Directory + filename)
        #     fin.write(client_connection)
        #     response = 'HTTP/1.0 200 OK\n\n'
        #     client_connection.sendall(response.encode())
        #     client_connection.close()

        else:
            with open(Directory+filename, 'rb') as file_to_send:
                for data in file_to_send:
                    client_connection.sendall(data)
                    response = 'HTTP/1.0 200 OK\n\n'
                    client_connection.sendall(response.encode())
                    client_connection.close()

    else:
        fin = open(Directory +'file1.html')
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
        client_connection.sendall(response.encode())
        client_connection.close()

    print('=================')
    start_new_thread(threaded, (client_connection,))
    if koneksi != 'keep-alive':
        break

# Close socket
server_socket.close()