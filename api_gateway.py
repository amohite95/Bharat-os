import http.server
import socketserver
import json
import time

PORT = 8080

class AmLabsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        response = {
            "company": "am_labs",
            "status": "ONLINE",
            "admin": "amohite95@gmail.com",
            "os_layer": "Bharat-os",
            "payment_gateway": "Pending Integration (Canara Bank)",
            "timestamp": time.time()
        }
        self.wfile.write(json.dumps(response).encode())

print("==================================================")
print(f"      am_labs // API GATEWAY ONLINE (PORT {PORT}) ")
print("==================================================")
print("[+] Listening for incoming client connections...")
print("[+] System architecture is active.")

with socketserver.TCPServer(("", PORT), AmLabsHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] API GATEWAY SHUTTING DOWN.")
