import random
import redis
from django.conf import settings
from django.core.mail import send_mail


class EmailVerifyService:
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
        )

    def create_code(self, data):
        email = data.get("email")

        # Generate a 6-digit random code
        code = random.randint(100000, 999999)

        # Store the code in Redis with a TTL (e.g., 10 minutes)
        self.redis_client.setex(
            f"email_verification:{email}", 600, code
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
        if stored_code is None or stored_code != code:
            return False

        self.redis_client.delete(f"email_verification:{email}")
        return True
