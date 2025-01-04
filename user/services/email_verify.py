import random

from django.conf import settings
from django.core.mail import send_mail

from commons.clients.redis_client import RedisClient


class EmailVerifyService:
    def __init__(self, redis_client=None):
        self.redis_client = redis_client or RedisClient()

    def create_code(self, data):
        email = data.get("email")

        # Generate a 6-digit random code
        code = random.randint(100000, 999999)

        # Store the code in Redis with a TTL (e.g., 10 minutes)
        self.redis_client.set(
            f"email_verification:{email}", code, 600
        )  # Key expires in 600 seconds

        # Send the code via email
        send_mail(
            subject="Your Verification Code",
            message=f"Your verification code is: {code}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )

    def verify(self, data):
        email = data.get("email")
        code = data.get("code")

        # Retrieve the code from Redis
        stored_code = self.redis_client.get(f"email_verification:{email}")
        if int(stored_code) is None or stored_code != code:
            return False

        self.redis_client.delete(f"email_verification:{email}")
        return True
