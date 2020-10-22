from rest_framework import routers
from django.urls import path, include
from .views import MyUserViewSet, AuthorViewSet, BookViewSet , SubscriberViewSet , SubscriptionViewSet


router = routers.DefaultRouter()

router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'books',BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'users', MyUserViewSet)
router.register(r'subscribers', SubscriberViewSet)


urlpatterns = [
    path('', include(router.urls)), # anything after url endpoint, taken care by router   
]
