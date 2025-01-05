from enum import Enum


class RedisKey(Enum):
    EMAIL_VERIFICATION = "email_verification"
    EMAIL_VERIFIED = "email_verified"
