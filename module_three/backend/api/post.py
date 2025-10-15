from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import os
import random

file_path = Path(os.getcwd()) / "backend/data.json"

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=201):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self):
        content_size = int(self.headers.get("Content-Length", 0))
        post_data = json.loads(self.rfile.read(content_size))

        if not file_path.exists():
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                output_data = json.load(f)
                if not isinstance(output_data, list):
                    output_data = []
            except json.JSONDecodeError:
                output_data = []

        # Check if email already exists
        user_emails = [item['email'] for item in output_data]
        if post_data['email'] in user_emails:
            print("Account already exists.")
            self.send_data({"Message": "Account already exists"}, status=409)
            return 

        # Append new user
        existing_ids = {item["id"] for item in output_data}
        new_id = random.randint(10, 99)
        while new_id in existing_ids:
            new_id = random.randint(10, 99)
        post_data["id"] = new_id
        
        output_data.append(post_data)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=4)

        print("New user added.")
        self.send_data({
            "Message": "Data Received",
            "data": post_data
        })
        return 

def run():
    HTTPServer(("localhost", 5000), BasicAPI).serve_forever()

print("Application is running...")
run()
