# udp_producer.py
import socket, time, json, random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('127.0.0.1', 9999)
i = 0
try:
    while True:
        payload = {"i": i, "value": random.randint(1,100)}
        sock.sendto(json.dumps(payload).encode('utf-8'), addr)
        print("sent:", payload)
        i += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("producer stopped")
