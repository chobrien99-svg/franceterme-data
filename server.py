#!/usr/bin/env python3
"""
Simple HTTP server to view the FranceTerme visualization
"""
import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("🇫🇷 FranceTerme Interactive Visualization Server")
        print("=" * 60)
        print(f"\n✨ Server running at: http://localhost:{PORT}")
        print(f"📂 Serving from: {os.getcwd()}")
        print("\n🚀 Opening browser...")
        print("\n⌨️  Press Ctrl+C to stop the server\n")

        # Open browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            print("Could not open browser automatically. Please open manually.")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped. Au revoir!")
