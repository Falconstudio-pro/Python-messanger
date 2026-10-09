import socket
import threading
import argparse
from cryptography.fernet import Fernet
from rich.console import Console

console = Console()


def load_key(path="secret.key"):
    with open(path, "rb") as f:
        return f.read()


class Server:
    def __init__(self, host, port, key):
        self.host = host
        self.port = port
        self.key = Fernet(key)
        self.clients = []

    def broadcast(self, message, sender=None):
        encrypted = self.key.encrypt(message.encode())
        for client in self.clients:
            if client != sender:
                try:
                    client.send(encrypted)
                except Exception:
                    pass

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(4096)
                if not data:
                    break

                message = self.key.decrypt(data).decode()
                console.print(f"[cyan]Nachricht:[/cyan] {message}")
                self.broadcast(message, sender=client)
            except Exception:
                break

        client.close()
        if client in self.clients:
            self.clients.remove(client)

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)

        console.print('[green][+] Server gestartet[/green]')
        console.print(f'[green][+] Lauscht auf {self.host}:{self.port}[/green]')

        while True:
            client, addr = server.accept()
            console.print(f'[green][+] Verbindung von {addr}[/green]')
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client,), daemon=True).start()


class Client:
    def __init__(self, host, port, username, key):
        self.username = username
        self.key = Fernet(key)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def receive(self):
        while True:
            try:
                data = self.sock.recv(4096)
                if not data:
                    break
                msg = self.key.decrypt(data).decode()
                console.print(f'\n[yellow]{msg}[/yellow]')
            except Exception:
                break

    def start(self):
        threading.Thread(target=self.receive, daemon=True).start()

        console.print('[green][+] Sichere Verbindung hergestellt[/green]')
        console.print('[green][+] Ende-zu-Ende-Verschlüsselung aktiv[/green]')

        while True:
            msg = input(f'{self.username} > ')
            full = f'{self.username}: {msg}'
            self.sock.send(self.key.encrypt(full.encode()))


def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as f:
        f.write(key)
    console.print('[green][+] secret.key erstellt[/green]')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Secure Messenger')
    parser.add_argument('--generate-key', action='store_true')
    parser.add_argument('--server', action='store_true')
    parser.add_argument('--client', action='store_true')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5555)
    parser.add_argument('--username', default='User')

    args = parser.parse_args()

    if args.generate_key:
        generate_key()
    elif args.server:
        Server(args.host, args.port, load_key()).start()
    elif args.client:
        Client(args.host, args.port, args.username, load_key()).start()
    else:
        parser.print_help()
