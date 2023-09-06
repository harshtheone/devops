import logging, time
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from neo4j import GraphDatabase
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAFKA_BROKER = 'kafka:9092'
ELASTICSEARCH_HOST = 'elasticsearch'
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_USERNAME = 'elastic'
ELASTICSEARCH_PASS = 'changeme'

NEO4J_HOST = 'bolt://neo4j:7687'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'some_password'
TOPIC = 'test-topic'


class Neo4jClient:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

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
            es = Elasticsearch(
                                [
                                    {
                                        'host':str(ELASTICSEARCH_HOST),
                                        'port':str(ELASTICSEARCH_PORT),
                                        'scheme': "http"
                                    }
                                ], 
                                http_auth=(str(ELASTICSEARCH_USERNAME), str(ELASTICSEARCH_PASS))
                            )

            # Initialize Neo4j client
            neo4j_client = Neo4jClient(NEO4J_HOST, NEO4J_USER, NEO4J_PASSWORD)
            
            break
        except Exception as e:
            logging.error(f"Connection Error: {e}")
            time.sleep(1)
    for msg in consumer:
        message = msg.value.decode('utf-8')
        logging.info(f"Received message: {message}")

        # Insert into Elasticsearch
        es.index(index='messages-test', body={'content': message+ "-" + str(datetime.now())})
        
        # Insert into Neo4j
        neo4j_client.insert_message(message)

    neo4j_client.close()


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as error:
            logger.error(f"Main function: {error}")
            time.sleep(20)                                                              # Wait for service to be up
            continue
