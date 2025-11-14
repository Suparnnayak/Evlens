"""
Example Vercel Serverless Function
This shows how to create API routes for Vercel

To use this:
1. Create api/ directory in project root
2. Create files like: api/auth/login.py, api/analyze.py
3. Each file exports a handler function
"""

from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "message": "Hello from Vercel serverless function!",
            "path": self.path
        }
        
        self.wfile.write(json.dumps(response).encode())
        return
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "message": "POST request received",
            "data": post_data.decode()
        }
        
        self.wfile.write(json.dumps(response).encode())
        return

