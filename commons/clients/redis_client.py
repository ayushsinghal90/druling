import redis
from django.conf import settings


class RedisClient:
    def __init__(self):
        self.client = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,  # Automatically decode byte strings to regular strings
        )

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
