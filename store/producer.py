
from kafka import KafkaProducer
import json
import os

KAFKA_SERVERS = [os.getenv('KAFKA_SERVER')]
TOPIC = os.getenv('KAFKA_TOPIC')

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

def produce_data(browser: str):
    data = {
        'user_data': {
            'browser': browser
        }
    }
    producer.send(TOPIC, data)
    producer.flush()
