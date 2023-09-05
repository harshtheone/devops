from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time
import logging

KAFKA_BROKER = 'kafka:9092'
TOPIC = 'test-topic'

def main():
    # Initialize Kafka producer
    while True:
        logging.info("Connecting to Kafka, ES, neo4j...")
        try:
            producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER],api_version=(0,11,5))
            break
        except NoBrokersAvailable as e:
            print(f"ERROR {e}")
            time.sleep(1)
    message_count = 0

    try:
        while True:
            message = f"Message {message_count}".encode('utf-8')
            logging.error(message)
            producer.send(TOPIC, value=message)
            logging.info(f"Sent: {message}")
            message_count += 1
            time.sleep(1)  # wait for 1 second
    except KeyboardInterrupt:
        print("Shutting down producer...")
    finally:
        producer.close()

if __name__ == "__main__":
    main()
