from http.server import BaseHTTPRequestHandler, HTTPServer
import json
# data = []

file_path = r"C:\Users\ncc666\Desktop\ai_engineering\module_three\backend\data.json"

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=201):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self):
        content_size = int(self.headers.get("Content-Length", 0))
        parsed_data = self.rfile.read(content_size)
        post_data = json.loads(parsed_data)
        f = open(file_path, "r", encoding="utf-8")
        output_data = json.load(f)
        print(output_data)
        if (len(output_data) != 0):
            output_data.append(post_data)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=4)
        else:
            data = []
            data.append(post_data)
            f = open(file_path, "w", encoding="utf-8")
            f.write(json.dumps(data))
        self.send_data({
            "Message": "Data Recieved",
            "data": post_data
        })
def run():
    HTTPServer(("localhost", 5000), BasicAPI).serve_forever()

print("Application is running...")
run()
