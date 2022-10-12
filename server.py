from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        print('path = ', self.path)
        if self.path == '/':
            self.path = '/index.html'

            file_to_open = open(self.path[1:]).read()
            self.send_response(200)

            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))

        elif os.path.isdir(self.path):
        
            try:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(os.listdir(self.path)).encode())
            except:
                file_to_open = 'File Not Found'
                self.send_response(404)
        
        else:
            try:
                with open(self.path, 'rb') as f:
                    data = f.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(data)
            # error handling skipped
            except Exception:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'File Not Found')

httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()