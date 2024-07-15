# server/main.py

import http.server
from router import handle_request
import json  
class EcommerceRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        handle_request(self, 'GET')

    def do_POST(self):
        handle_request(self, 'POST')

    def do_PUT(self):
        handle_request(self, 'PUT')

    def do_DELETE(self):
        handle_request(self, 'DELETE')

    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, EcommerceRequestHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()
