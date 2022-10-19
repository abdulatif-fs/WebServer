from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import http.server
import socketserver


Path = 'C:/Users/ASUS/OneDrive/Dokumen/Abdulatif/kuliah/sem9/progjar/WebServer/utama/'
newdir = os.path.dirname(Path)
class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        filename= self.path.replace("/", '')
         
        print('path = ', self.path)
        # print(os.path.join(Path, self.path))
        # dir_list = os.listdir(self.path)
        # print('dirlist = ', dir_list)
        # print()
        if self.path == '/':
            self.path = '/index.html'

            file_to_open = open(newdir+'/'+self.path[1:]).read()
            self.send_response(200)

            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))

        elif filename not in os.listdir(newdir):
        
            self.path = '/404.html'

            file_to_open = open(newdir+self.path).read()
            self.send_response(404)

            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        
        elif '.' in self.path:
            if "html" in self.path:
                file_to_open = open(newdir+self.path).read()
                self.send_response(200)

                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
            else:
                with open(newdir+self.path, 'rb') as f:
                    data = f.read()
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(data)
        else:
        # try:
            # with open(newdir+self.path, 'rb') as f:
            #     data = f.read()
            #     self.send_response(200)
            #     self.end_headers()
            #     self.wfile.write(data)
        # error handling skipped
        # except Exception:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Folder menyusul')

httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()