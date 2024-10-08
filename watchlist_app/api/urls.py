from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamDetailAV, ReviewList, ReviewDetail, ReviewCreate, UserReview, SearchWatchList

# router = DefaultRouter()
# router.register('stream',StreamPlatformAV.as_view(), basename='streamplatform')

urlpatterns = [
    path('list/',WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/',WatchDetailAV.as_view(), name='watch-detail'),
    path('list2/', SearchWatchList.as_view(), name='watch-list'),
    # path('', include(router.urls)),
    path('stream/',StreamPlatformAV.as_view(), name='stream-platform'),#Only by Admin
    # path('stream/<int:pk>', StreamDetailAV.as_view(), name= 'stream-detail'),
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/',ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('reviews/', UserReview.as_view(), name='review_user-detail'),


    
]
