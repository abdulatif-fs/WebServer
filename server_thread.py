import socket
import os
import konfig
from _thread import *
import threading

CRLF= "\r\n"
# print_lock = threading.Lock()
# class ClientThread(threading.Thread):
#     def __init__(self,client_address, client_connection):
#         threading.Thread.__init__(self)
def thread(client_connection, client_address):
    # csocket = client_connection
    print('========================')
    print ("New connection added: ", client_address)

    while True:
        request = client_connection.recv(1024).decode()
        # print(request)
        headers = request.split('\n')
        filename = headers[0].split()[1]
        # print('request nya nihh:', filename)
        indexname = filename.replace('/','')
        # print('index name:',indexname,'==')
        hostname = headers[1].split(':')[1]
        print(hostname, ' Terhubung ......')
        koneksi = headers[2].split()[1]
        print('connection: ', koneksi)

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
            response = 'HTTP/1.0 200 OK'+CRLF+'Content-Type: text/html' + CRLF*2 + content
            client_connection.sendall(response.encode())
            client_connection.close()
        
        elif indexname not in os.listdir(newdir):
                fin = open(Directory + '/404.html')
                content = fin.read()
                fin.close()

                response = 'HTTP/1.0 404 Not Found'+CRLF
                client_connection.sendall(response.encode())
                client_connection.close()

        elif '.' in filename:        
     # Get the content of htdocs/index.html        
            if 'html' in filename:
                fin = open(Directory + filename)
                content = fin.read()
                fin.close()
                # Send HTTP response
                tipe = 'text/html'
                response = 'HTTP/1.0 200 OK'+CRLF+'Content-Type: '+tipe+CRLF*2+ content
                client_connection.sendall(response.encode())
                client_connection.close()

            elif 'pdf' in filename:
                with open(Directory+filename, 'rb') as file_to_send:
                        tipe = 'application/pdf'
                        response = 'HTTP/1.0 200 OK'+CRLF+'Content-Type: '+tipe+CRLF*2
                        client_connection.sendall(response.encode())
                        client_connection.sendfile(file_to_send)
                        client_connection.close()
            
            elif 'png' in filename:
                with open(Directory+filename, 'rb') as file_to_send:
                        # tipe = 'video/mp2t'
                        tipe = 'image/pn'
                        response = 'HTTP/1.0 200 OK'+CRLF+'Content-Type: '+tipe+CRLF*2
                        client_connection.sendall(response.encode())
                        client_connection.sendfile(file_to_send)
                        client_connection.close()
            
            elif 'rar' in filename:
                with open(Directory+filename, 'rb') as file_to_send:
                        # tipe = 'video/mp2t'
                        tipe = 'application/vnd.ra'
                        response = 'HTTP/1.0 200 OK'+CRLF+'Content-Type: '+tipe+CRLF*2
                        client_connection.sendall(response.encode())
                        client_connection.sendfile(file_to_send)
                        client_connection.close()

            else:
                with open(Directory+filename, 'rb') as file_to_send:
                    # for data in file_to_send:
                        # client_connection.sendall(data)
                        # tipe = 'image/pn'
                        response = 'HTTP/1.0 200 OK'+CRLF
                        client_connection.sendall(response.encode())
                        client_connection.sendfile(file_to_send)
                        client_connection.close()
    
        else:
            fin = open(Directory +'file1.html')
            content = fin.read()
            fin.close()

            response = 'HTTP/1.0 200 OK\n\n' + content
            client_connection.sendall(response.encode())
            client_connection.close()
        # print_lock.release()
        # csocket.close()
        print('====================')


host = '127.0.0.1'
port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port)) 
server_socket.listen(1)
print( '%s is Activated ...' % host)
print('Listening on port %s ...' % port)
while True:

    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    # print_lock.acquire()
    start_new_thread(thread, (client_connection,client_address))