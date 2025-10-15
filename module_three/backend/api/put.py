from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import os
from urllib.parse import urlparse

file_path = Path(os.getcwd()) / "backend/data.json"

class BasicAPI(BaseHTTPRequestHandler):
  def send_data(self, payload, status=200):
    """Send JSON response to client"""
    self.send_response(status)
    self.send_header("Content-Type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(payload).encode())

  def do_PUT(self):
    # Get request body
    content_size = int(self.headers.get("Content-Length", 0))
    post_data = json.loads(self.rfile.read(content_size))
    
    parsed_url = urlparse(self.path)
    path_parts = parsed_url.path.strip("/").split("/")
    user_id = path_parts[-1]

    if not user_id:
      self.send_data({"Message": "Add id as a path parameter"}, status=400)
      return

    if not file_path.exists():
      self.send_data({"Message": "Data file not found"}, status=404)
      return

    with open(file_path, "r", encoding="utf-8") as f:
      output_data = json.load(f)

    user_found = False

    for item in output_data:
      if str(item["id"]) == str(user_id):  
        item["name"] = post_data.get("name", item["name"])
        item["email"] = post_data.get("email", item["email"])
        item["password"] = post_data.get("password", item["password"])
        user_found = True
        break

    if not user_found:
      self.send_data({"Message": "User ID not found"}, status=404)
      return

    # Save updated data
    with open(file_path, "w", encoding="utf-8") as f:
      json.dump(output_data, f, indent=2)

    # Send success response
    self.send_data({
      "Message": "User updated successfully",
      "data": post_data
    }, status=201)

def run():
  server = HTTPServer(("localhost", 3000), BasicAPI)
  print("Application is running on port 3000...")
  server.serve_forever()

run()
