from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import os
import random
from urllib.parse import urlparse

file_path = Path(os.getcwd()) / "backend/data.json"

class BasicAPI(BaseHTTPRequestHandler):
  def send_data(self, payload, status=201):
    self.send_response(status)
    self.send_header("Content-Type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(payload).encode())

  def do_DELETE(self):
    with open(file_path, "r", encoding="utf-8") as f:
      output_data = json.load(f)
    
    parsed_url = urlparse(self.path)
    path_parts = parsed_url.path.strip("/").split("/")
    user_id = str(path_parts[-1])
    print(user_id)

    user_ids = [item['id'] for item in output_data]
    print(user_ids)
    for item in output_data:
      if str(item["id"]) != str(user_id):
        print("Account does not exist.")
        self.send_data({"Message": "Account does not exist"}, status=401)
        return 
      else:
        result = next((item for item in output_data if str(item["id"]) == str(user_id)))
        print(result)     
        output_data.remove(result)
      with open(file_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4)

    print("Account deleted successfully.")
    self.send_data({
      "Message": "Account deleted successfully"
    })
    print(output_data)
    return 

def run():
    HTTPServer(("localhost", 5000), BasicAPI).serve_forever()

print("Application is running...")
run()
