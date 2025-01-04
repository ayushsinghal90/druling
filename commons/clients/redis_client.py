import redis
import json
from django.conf import settings


class RedisClient:
    def __init__(self):
        self.client = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,  # Automatically decode byte strings to regular strings
        )

    def client(self):
        return self.client

    def set(self, key, value, ttl=None):
        """
        Set a key-value pair in Redis with an optional TTL (time-to-live).
        :param key: Redis key
        :param value: Redis value
        :param ttl: Time-to-live in seconds (optional)
        """
        if ttl:
            self.client.setex(key, ttl, value)
        else:
            self.client.set(key, value)

    def get(self, key):
        """
        Get a value from Redis by key.
        :param key: Redis key
        :return: Value or None if the key does not exist
        """
        return self.client.get(key)

    def set_hash(self, key, data):
        """Store a dictionary in Redis."""
        self.client.hset(key, mapping=data)

    def get_hash(self, key):
        """Retrieve a dictionary from Redis."""
        return self.client.hgetall(key)

    def set_json(self, key, data, ttl=None):
        """Store a JSON-serializable object in Redis."""
        json_data = json.dumps(data)
        self.set(key, json_data, ttl)

    def get_json(self, key):
        """Retrieve and deserialize a JSON object from Redis."""
        json_data = self.get(key)
        return json.loads(json_data) if json_data else None

    def delete(self, key):
        """
        Delete a key from Redis.
        :param key: Redis key
        """
        self.client.delete(key)

    def exists(self, key):
        """
        Check if a key exists in Redis.
        :param key: Redis key
        :return: True if the key exists, False otherwise
        """
        return self.client.exists(key) > 0

    def increment(self, key, amount=1):
        """
        Increment a key's value by a specified amount.
        :param key: Redis key
        :param amount: Increment amount (default is 1)
        :return: New value after increment
        """
        return self.client.incr(key, amount)

    def expire(self, key, ttl):
        """
        Set an expiration time for a key.
        :param key: Redis key
        :param ttl: Time-to-live in seconds
        """
        self.client.expire(key, ttl)
