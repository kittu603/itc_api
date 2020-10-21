from django.urls import path, include
from .views import BookListView, AuthorListView , MyUserListView , SubscriberListView, SubscriptionListView

urlpatterns = [
    path('books/',BookListView.as_view()),
    path('authors/', AuthorListView.as_view()),
    path('users/', MyUserListView.as_view()),
    path('subscribers/', SubscriberListView.as_view()),
    path('subscriptions/', SubscriptionListView.as_view()),
]
