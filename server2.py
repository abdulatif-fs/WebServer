import socket
# import socketserver
# import http.server

host = '127.0.0.1'
port = 8080
Path = 'C:/Users/ASUS/OneDrive/Dokumen/Abdulatif/kuliah/sem9/progjar/WebServer'
# Create socket
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
    # print('request nya nihh : ', filename)

    hostname = headers[1].split(':')[1]
    print(hostname, ' Terhubung ......')

    #direktori dan konfigurasi
    if hostname == ' abdulatif.com':
        Directory = 'C:/Users/ASUS/OneDrive/Dokumen/Abdulatif/kuliah/sem9/progjar/WebServer/folder1/'
    elif hostname == ' fajar.co.id':
        Directory = 'C:/Users/ASUS/OneDrive/Dokumen/Abdulatif/kuliah/sem9/progjar/WebServer/folder2/'

     # Get the content of htdocs/index.html
    if filename == '/':
        filename = '/index.html'

        fin = open(Directory + filename)
        content = fin.read()
        fin.close()

        # Send HTTP response
        response = 'HTTP/1.0 200 OK\n\n' + content
        client_connection.sendall(response.encode())
        client_connection.close()
    elif filename == '/index.html':
        fin = open(Directory + filename)
        content = fin.read()
        fin.close()

        # Send HTTP response
        response = 'HTTP/1.0 200 OK\n\n' + content
        client_connection.sendall(response.encode())
        client_connection.close()
    elif filename == '/folder1':
        fin = open(Directory +'file1.html')
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
        client_connection.sendall(response.encode())
        client_connection.close()
    else:
        response = 'HTTP/1.0 404 Not Found\n\n'
        client_connection.sendall(response.encode())
        client_connection.close()

    print('=================')

# Close socket
server_socket.close()