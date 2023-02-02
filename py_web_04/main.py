import mimetypes
import pathlib
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import socket
import json
from datetime import datetime
from threading import Thread


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == "/":
            self.set_html_file("./static/index.html")
        elif pr_url.path == "/message":
            self.set_html_file("./static/message.html")
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.set_html_file("./static/error.html", 404)

    def do_POST(self):
        data = self.rfile.read(int(self.headers["Content-Length"]))
        run_client(data)
        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()

    def set_html_file(self, filename: str, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as file:
            self.wfile.write(file.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())


def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = "localhost", 5000
    sock.bind(server)

    try:
        while True:
            data, address = sock.recvfrom(1024)
            input_data = data.decode()
            print(f"Received data: {input_data} from {address}")
            data_parse = urllib.parse.unquote_plus(input_data)
            data_dict = {
                key: value
                for key, value in [el.split("=") for el in data_parse.split("&")]
            }
            file_to_save = pathlib.Path(".\storage\data.json")
            key_to_save = str(datetime.now())

            if file_to_save.stat().st_size == 0:
                with open(file_to_save, "w") as file:
                    json.dump({key_to_save: data_dict}, file, indent=4)
            else:
                with open(file_to_save, "r") as file:
                    src = json.load(file)
                    src.update({key_to_save: data_dict})

                with open(file_to_save, "w") as file:
                    json.dump(src, file, indent=4)
            print(f"Mission accomplished.")

    except KeyboardInterrupt:
        print(f"Destroy server.")

    finally:
        sock.close()


def run_client(data: bytes):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = "localhost", 5000
    sock.sendto(data, server)
    sock.close()


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler):
    server_address = ("localhost", 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    echo_server = Thread(target=run_server).start()
    run()