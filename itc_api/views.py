from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Author, Book , MyUser, Subscription,Subscriber
from .serializers import BookSerializer, AuthorSerializer, MyUserSerializer , SubscriberSerializer, SubscriptionSerializer
# Create your views here.

class MyUserListView(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SubscriberListView(ListAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class SubscriptionListView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
