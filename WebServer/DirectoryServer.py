import os
from http.server import HTTPServer, CGIHTTPRequestHandler

##############
# This server gives the ability to browse a target directory via web browser
##############

# Use the current directory for the server
os.chdir('.')

# Create server object listening the port 80
# CGI ->  Common Gateway Interface: interface specification for web servers to 
#         execute programs like console applications running on a server that 
#         generates web pages dynamically
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)

# Start the web server
server_object.serve_forever()