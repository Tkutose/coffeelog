
from rest_framework.throttling import UserRateThrottle

class UserUploadsThrottle(UserRateThrottle):
    scope = 'uploads'
