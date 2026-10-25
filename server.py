import socket
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

# Shared secret key
KEY = base64.b64decode("wNYKnFCdujY38oeXtf48sY6UOQ/0kZn+sW6+puFiUUE=")
aesgcm = AESGCM(KEY)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5555))
server.listen(1)

print("[*] Server is listening on port 5555...")
print("[*] Waiting for client to connect...")

conn, addr = server.accept()
print(f"[+] Client connected from {addr}")

while True:
    data = conn.recv(4096)
    if not data:
        break

    try:
        nonce = data[:12]
        ciphertext = data[12:]
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        print(f"\n[Client]: {plaintext.decode()}")
    except Exception:
        print("[!] Failed to decrypt message")

    message = input("You: ")
    if message.lower() == "exit":
        break

    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, message.encode(), None)
    conn.send(nonce + ciphertext)

conn.close()
server.close()
print("[*] Connection closed")