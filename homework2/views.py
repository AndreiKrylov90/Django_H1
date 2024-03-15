from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .forms import AuthorForm, PostForm, ProductForm
from .models import User2, Product2, Order2, Author, Post
import datetime


def user_products(request, user_id, days):
    user = get_object_or_404(User2, pk=user_id)
    orders = Order2.objects.filter(customer=user, date_ordered__gte=timezone.now() - datetime.timedelta(days=days))
    products = set()

    for order in orders:
        products.update(order.products.all())

    context = {'user': user, 'days': days, 'products': products}
    return render(request, 'homework2/user_products.html', context)


def authors(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Author(**form.cleaned_data).save()
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {
        "title": "Авторы",
        "authors": authors,
        'form': form,
    }
    return render(request, 'homework2/authors.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    context = {
        "post": post,
    }
    return render(request, 'homework2/post.html', context)


def user_posts(request, user_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = get_object_or_404(Author, pk=user_id)
            Post.objects.create(author=author, **form.cleaned_data)
    else:
        form = PostForm()

    user = get_object_or_404(Author, pk=user_id)
    posts = Post.objects.filter(author=user)
    context = {
        "title": "Посты",
        "author": user,
        "posts": posts,
        'form': form,
    }
    return render(request, 'homework2/posts.html', context)


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product2(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                amount=form.cleaned_data['amount'],
                photo=form.cleaned_data['photo']
            )
            product.save()
    else:
        form = ProductForm()
    products = Product2.objects.all()
    context = {
        "title": "Продукты",
        "products": products,
        'form': form,
    }
    return render(request, 'homework2/product.html', context)
