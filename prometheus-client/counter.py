import http.server
from prometheus_client import start_http_server, Counter

REQUEST_COUNT = Counter("app_requests_count", "total app http requestcount")

APP_PORT = 18080
METRICS_PORT = 18081


class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST_COUNT.inc()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Counter</h1>")


if __name__ == "__main__":
    # metrics 서버를 모든 인터페이스에 바인딩
    start_http_server(METRICS_PORT, addr="0.0.0.0")
    print(f"Metrics server started on 0.0.0.0:{METRICS_PORT}")

    # 애플리케이션 서버도 모든 인터페이스에 바인딩 (필요하다면)
    server = http.server.HTTPServer(("0.0.0.0", APP_PORT), HandleRequests)
    print(f"Application server started on 0.0.0.0:{APP_PORT}")
    server.serve_forever()
