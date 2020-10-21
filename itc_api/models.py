from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    name = models.CharField(max_length=25)
    address = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    count = models.PositiveIntegerField()
    subscription_cost = models.PositiveIntegerField()
    topic = models.CharField(max_length=20)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.user}"







class Subscription(models.Model):
    subscriber = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.PositiveIntegerField(default=0)
    days = models.PositiveIntegerField(default=0)
    returned = models.BooleanField()

    def __str__(self):
        return f"{self.subscriber} subscribed to {self.book}"


class New:
    pass






