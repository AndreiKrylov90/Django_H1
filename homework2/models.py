from django.db import models
from django.utils import timezone


class User2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}'


class Product2(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product #{self.pk}: {self.name}, price: {self.price}, amount: {self.amount}'


class Order2(models.Model):
    customer = models.ForeignKey(User2, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        products = ', '.join([product.name for product in self.products.all()])
        return f'Order: customer: {self.customer.name}, total_price: {self.total_price}, products: {products}'

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    lastname = models.CharField(max_length=100)
    biography = models.TextField()
    date_of_birth = models.DateTimeField(default=timezone.now())


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'
