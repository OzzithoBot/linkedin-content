#!/usr/bin/env python3
"""Servidor web para LinkedIn Content - Windows compatible"""
import http.server
import json
import os
import sys
from pathlib import Path

PORT = 8765
BASE_DIR = Path(__file__).parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)
    
    def do_GET(self):
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            data_file = BASE_DIR / 'data.json'
            if data_file.exists():
                with open(data_file, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'{"posts":[],"stats":{},"total":0}')
        else:
            super().do_GET()

if __name__ == '__main__':
    print(f"Servidor iniciado en http://localhost:{PORT}")
    print(f"Directorio: {BASE_DIR}")
    server = http.server.HTTPServer(('127.0.0.1', PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido")
