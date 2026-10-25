# Secure Communication Channel using AES-256

This project implements a secure communication channel between a client and a server using **AES-256-GCM** encryption.

## Features
- AES-256 encryption (symmetric encryption)
- Secure message transmission over TCP sockets
- Client and Server can send and receive encrypted messages
- Messages are automatically decrypted on the receiving side

## How to Run

1. Install the required library:
```bash
pip install cryptography