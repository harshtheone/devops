from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from neo4j import GraphDatabase
import logging

KAFKA_BROKER = 'kafka:9092'
ELASTICSEARCH_HOST = 'elasticsearch'
NEO4J_HOST = 'bolt://neo4j:7687'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'some_password'
TOPIC = 'test-topic'


class Neo4jClient:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password),api_version=(0,11,5))

    def close(self):
        self._driver.close()

    def insert_message(self, message):
        with self._driver.session() as session:
            session.write_transaction(self._create_message, message)

    @staticmethod
    def _create_message(tx, message):
        tx.run("CREATE (message:Message {content: $content})", content=message)


def main():
    while True:
        try:
            logging.info("Connecting to Kafka, ES, neo4j...")
            # Initialize Kafka consumer
            consumer = KafkaConsumer(TOPIC, bootstrap_servers=[KAFKA_BROKER])

            # Initialize Elasticsearch client
            es = Elasticsearch([ELASTICSEARCH_HOST])

            # Initialize Neo4j client
            neo4j_client = Neo4jClient(NEO4J_HOST, NEO4J_USER, NEO4J_PASSWORD)
            
            break
        except Exception as e:
            print(f"ERROR {e}")
            time.sleep(1)
    for msg in consumer:
        message = msg.value.decode('utf-8')
        print(f"Received message: {message}")

        # Insert into Elasticsearch
        es.index(index='messages', body={'content': message})

        # Insert into Neo4j
        neo4j_client.insert_message(message)

    neo4j_client.close()


if __name__ == "__main__":
    main()
