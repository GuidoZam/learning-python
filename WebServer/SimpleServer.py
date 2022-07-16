#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomServer(BaseHTTPRequestHandler):
    # GET method
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        # This will be the response message
        message = "I'm a web page!"
        self.wfile.write(bytes(message, "utf8"))
        return
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data_posted = self.rfile.read(content_length)
        print(data_posted)
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    print('Starting up server...')
    # Set the server address and port
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, CustomServer)
    print('Server is listening...')
    httpd.serve_forever()

run()