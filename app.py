#!/usr/bin/env python3
"""
AirWrite — Desktop Application Launcher
Serves index.html over a local HTTP server and opens default web browser.
Can be compiled to a standalone executable via PyInstaller.
"""

import http.server
import os
import socketserver
import sys
import threading
import time
import webbrowser

PORT = 8520

def get_base_dir():
    """Get absolute path to resource, works for dev and PyInstaller bundle"""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=get_base_dir(), **kwargs)

    def log_message(self, format, *args):
        # Suppress routine HTTP request logging to keep console clean
        pass

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler) as httpd:
        httpd.serve_forever()

def main():
    print("=" * 50)
    print("  ✍ AirWrite — Neon Air Drawing Studio")
    print(f"  Local Server: http://127.0.0.1:{PORT}")
    print("=" * 50)
    print("Starting background server and launching browser...")

    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    time.sleep(0.5)
    webbrowser.open(f"http://127.0.0.1:{PORT}/index.html")

    print("AirWrite is running! Press Ctrl+C in this terminal to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down AirWrite...")
        sys.exit(0)

if __name__ == "__main__":
    main()
