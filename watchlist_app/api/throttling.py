from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrot(UserRateThrottle):
    scope = 'review-create'

class ReviewListThrot(UserRateThrottle):
    scope = 'review-list'