import http.server
from prometheus_client import start_http_server

APP_PORT = 18080

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Counter</h1>')
        # self.wfile.close()

if __name__ == '__main__':
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    print(f'Server started on localhost:{APP_PORT}')
    server.serve_forever()
    print('Server stopped')
