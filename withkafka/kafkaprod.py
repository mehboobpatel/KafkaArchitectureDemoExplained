from confluent_kafka import Producer
import time, json, random

conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

topic = "demo-topic"

def delivery_report(err, msg):
    if err:
        print("Delivery failed:", err)
    else:
        # decode the payload back for pretty printing
        print(f"Delivered: {msg.value().decode('utf-8')} "
              f"to {msg.topic()} [partition {msg.partition()}] @ offset {msg.offset()}")

i = 0
try:
    while True:
        data = {"i": i, "value": random.randint(1,100)}
        payload = json.dumps(data).encode('utf-8')
        producer.produce(topic, payload, callback=delivery_report)
        producer.poll(0)  # triggers delivery_report
        print("Produced:", data)   # <-- print payload here
        i += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("Producer stopped")
