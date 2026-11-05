from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).parent)
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(204); self.end_headers(); return
        super().do_GET()
ThreadingHTTPServer(("localhost",8000),QuietHandler).serve_forever()
