# udp_consumer.py
import socket, json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 9999))
print("UDP consumer listening on 0.0.0.0:9999")
try:
    while True:
        data, addr = sock.recvfrom(65536)
        print("received:", json.loads(data.decode('utf-8')))
except KeyboardInterrupt:
    print("consumer stopped")
