# Kafka Demo Project

## Overview

This project demonstrates how to use [Apache Kafka](https://kafka.apache.org/) for building distributed, scalable, and fault-tolerant messaging systems. It contains two main implementations:

- **withkafka/**: Uses the `confluent_kafka` Python client to interact with Kafka.
- **withoutkafka/**: Provides alternative producer/consumer logic without Kafka.

---

## Use Case

**Layman Terms:**
Imagine you have many apps or services that need to talk to each other, like a food delivery app where orders, payments, and notifications all need to be coordinated. Kafka acts like a post office, making sure messages (like "new order placed") are delivered reliably and quickly to the right place.

**Technical Terms:**
Kafka is used for real-time data streaming, event-driven architectures, decoupling microservices, and building robust logging/monitoring pipelines. It allows multiple producers and consumers to exchange data asynchronously and at scale.

---

## Kafka Architecture & Jargon Explained

### 1. Topic
- **Layman:** A topic is like a named mailbox where messages are dropped off and picked up.
- **Technical:** Topics are logical channels in Kafka to which producers send messages and from which consumers read. Each topic can have multiple partitions.

### 2. Broker
- **Layman:** A broker is like a post office branch that stores and manages mailboxes (topics).
- **Technical:** A broker is a Kafka server that stores data and serves client requests. Kafka clusters have multiple brokers for scalability and fault tolerance.

### 3. Producer
- **Layman:** A producer is someone who sends a letter (message) to a mailbox (topic).
- **Technical:** Producers are applications that publish (write) messages to Kafka topics. They can send data to specific topics and partitions.

### 4. Partition
- **Layman:** Partitions are like separate slots in a mailbox, allowing mail to be sorted and accessed faster.
- **Technical:** Each topic is split into partitions. Partitions allow Kafka to scale horizontally and enable parallel processing. Each partition is an ordered, immutable sequence of messages.

### 5. Consumer
- **Layman:** A consumer is someone who checks the mailbox and reads the letters (messages).
- **Technical:** Consumers subscribe to topics and read messages. They can be grouped for load balancing and fault tolerance.

### 6. Offset
- **Layman:** Offset is like a bookmark showing which letters have already been read.
- **Technical:** Each message in a partition has a unique offset. Consumers use offsets to keep track of their position in the stream.

### 7. Replication Factor
- **Layman:** Replication is like making copies of each letter and storing them in different post offices, so nothing is lost if one office closes.
- **Technical:** Replication factor determines how many copies of each partition are kept across brokers. This ensures data durability and availability.

---

## How Kafka Is Used in This Project

- The [withkafka/docker-compose.yml](withkafka/docker-compose.yml) file sets up Kafka and Zookeeper using Docker for easy local development.
- [withkafka/kafkaprod.py](withkafka/kafkaprod.py): Implements a Kafka producer using `confluent_kafka.Producer`. It sends messages to a specified topic.
- [withkafka/kafkacons.py](withkafka/kafkacons.py): Implements a Kafka consumer using `confluent_kafka.Consumer`. It subscribes to a topic and reads messages.
- Topics are created automatically when producers send messages if they do not already exist.
- Brokers are managed by Docker Compose and are accessible on `localhost:9092`.

---

## Producer/Consumer Logic (withkafka)

### Producer (`kafkaprod.py`)
- Connects to Kafka broker.
- Sends messages to a topic (e.g., `test_topic`).
- Messages can be simple strings, JSON, or any serializable format.
- Example message format:
   ```python
   {"order_id": 123, "status": "placed", "timestamp": "2025-09-19T12:00:00Z"}
   ```

### Consumer (`kafkacons.py`)
- Connects to Kafka broker.
- Subscribes to the same topic.
- Continuously polls for new messages.
- Processes each message (e.g., prints, stores, or triggers an action).

### Message Format
- Messages are typically serialized as strings or JSON.
- Example:
   ```json
   {"user": "alice", "action": "login", "time": "2025-09-19T12:01:00Z"}
   ```

---

## Sequential Flow of Data
1. **Producer** creates a message and sends it to a Kafka topic.
2. **Kafka Broker** receives the message and stores it in the appropriate partition of the topic.
3. **Consumer** subscribes to the topic and reads messages from the partition, using offsets to track progress.
4. If a broker fails, other brokers with replicated data ensure no messages are lost.

---

## Project Structure

```
withkafka/
   docker-compose.yml      # Kafka and Zookeeper containers
   exec.sh                 # Helper script for execution
   kafkacons.py            # Kafka consumer
   kafkaprod.py            # Kafka producer
   requirements.txt        # Python dependencies
   kafenv/                 # Python virtual environment
withoutkafka/
   cons.py                 # Consumer logic without Kafka
   prod.py                 # Producer logic without Kafka
```

---

## Running the Project

1. **Start Kafka and Zookeeper:**
    ```sh
    cd withkafka
    docker-compose up
    ```

2. **Install dependencies:**
    ```sh
    python3 -m venv kafenv
    source kafenv/bin/activate
    pip install -r requirements.txt
    ```

3. **Run Producer:**
    ```sh
    python kafkaprod.py
    ```

4. **Run Consumer:**
    ```sh
    python kafkacons.py
    ```

---

## References

- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Confluent Kafka Python Client](https://github.com/confluentinc/confluent-kafka-python)

---

## Summary

Kafka is a powerful tool for building scalable, reliable, and real-time data pipelines. This project provides hands-on examples of how to produce and consume messages, with clear explanations of the core concepts and architecture. Whether you're new to Kafka or looking to deepen your understanding, this repository is a practical starting point.