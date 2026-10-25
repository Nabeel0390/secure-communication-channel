import socket
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

# Shared secret key (must be the same as server)
KEY = base64.b64decode("wNYKnFCdujY38oeXtf48sY6UOQ/0kZn+sW6+puFiUUE=")
aesgcm = AESGCM(KEY)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

print("[*] Connected to server!")
print("Type your messages below. Type 'exit' to quit.\n")

while True:
    message = input("You: ")
    if message.lower() == "exit":
        break

    # Encrypt the message
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, message.encode(), None)
    client.send(nonce + ciphertext)

    # Receive and decrypt reply
    data = client.recv(4096)
    if not data:
        break

    try:
        nonce = data[:12]
        ciphertext = data[12:]
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        print(f"[Server]: {plaintext.decode()}")
    except Exception:
        print("[!] Failed to decrypt message")

client.close()
print("[*] Disconnected")