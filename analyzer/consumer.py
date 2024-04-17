
from threading import Thread
import json
from kafka import KafkaConsumer
import redis
import os

KAFKA_SERVERS = [os.getenv('KAFKA_SERVER')]
TOPIC = os.getenv('KAFKA_TOPIC')
REDIS_HOST = os.getenv('REDIS_HOST')

cache = redis.Redis(host=REDIS_HOST, decode_responses=True)

def get_cache() -> dict[str, int]:
    return {key: int(cache.get(key)) for key in cache.scan_iter()}

def consume():
    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_SERVERS,
        value_deserializer=json.loads,
        auto_offset_reset="latest",
    )
    consumer.subscribe(TOPIC)
    
    for data in consumer:
        key = data.value['user_data']['browser']
        cache.incr(key)

def launch_consumer():
    t = Thread(target=consume)
    t.start()
