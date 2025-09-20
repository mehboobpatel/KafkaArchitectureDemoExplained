docker exec -ti kafka bash

kafka-topics --create --bootstrap-server localhost:9092 \
  --replication-factor 1 --partitions 1 --topic demo-topic

kafka-topics --list --bootstrap-server localhost:9092
# should show: demo-topic
kafka-topics --describe --bootstrap-server localhost:9092 --topic demo-topic

kafka-topics --delete --bootstrap-server localhost:9092 --topic demo-topic

kafka-topics --alter \
  --bootstrap-server localhost:9092 \
  --topic demo-topic \
  --partitions 3


