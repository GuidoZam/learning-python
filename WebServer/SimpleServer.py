#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer

# Creiamo la classe che riceverà e risponderà alla richieste HTTP
class CustomServer(BaseHTTPRequestHandler):
    # Implementiamo il metodo che risponde alle richieste GET
    def do_GET(self):
        # Specifichiamo il codice di risposta
        self.send_response(200)
        # Specifichiamo uno o più header
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Specifichiamo il messaggio che costituirà il corpo della risposta
        message = "I'm a web page!"
        self.wfile.write(bytes(message, "utf8"))
        return
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    print('Avvio del server...')
    # Specifichiamo le impostazioni del server
    # Scegliamo la porta 8081 (per la porta 80 sono necessari i permessi di root)
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, CustomServer)
    print('Server in esecuzione...')
    httpd.serve_forever()

run()