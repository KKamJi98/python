import http.server
import random
import time
from prometheus_client import start_http_server, Gauge

REQUEST_INPROGRESS = Gauge('app_request_inprogress', 'number of application requests in progress')
REQUEST_LAST_SERVED = Gauge('app_last_served', 'time of the last request served')


APP_PORT = 18080
METRICS_PORT = 18081

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST_INPROGRESS.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Gauge</h1>')
        
        REQUEST_LAST_SERVED.set(time.time())
        REQUEST_INPROGRESS.dec()

if __name__ == '__main__':
    # metrics 서버를 모든 인터페이스에 바인딩
    start_http_server(METRICS_PORT, addr='0.0.0.0')
    print(f'Metrics server started on 0.0.0.0:{METRICS_PORT}')
    
    # 애플리케이션 서버도 모든 인터페이스에 바인딩 (필요하다면)
    server = http.server.HTTPServer(('0.0.0.0', APP_PORT), HandleRequests)
    print(f'Application server started on 0.0.0.0:{APP_PORT}')
    server.serve_forever()
