from django.shortcuts import render, redirect
from .models import *


def home_page(request):
    books = Books.objects.all()
    return render(request, 'home.html', {'books': books})







def create_author(request):
    author = Author.objects.all()
    if request.method == 'POST':
        Author.objects.create(
            name=request.POST['name'],
            age=request.POST['age'])
        return redirect('see_author')
    return render(request, 'create_author.html', {'author': author})



def see_author(request):
    author = Author.objects.all()
    return render(request, 'see_author.html', {'author': author})

def update_author(request, id):
    author = Author.objects.get(pk=id)
    if request.method == "POST":
        author.name = request.POST["name"]
        author.age = request.POST["age"]
        author.save()
        return redirect('see_author')
    return render(request, 'update_author.html', {'author': author})

def delete_author(request, id):
    author = Books.objects.get(pk=id)
    author.delete()
    return redirect('see_author')






def create_books(request):
    books = Books.objects.all()
    if request.method == 'POST':
        Books.objects.create(
            author_id=request.POST['author'],
            name=request.POST['name'],
            caption=request.POST['caption'],
            )
        return redirect('see_books')
    return render(request, 'create_books.html', {'author': Author.objects.all(),'books': books})




def see_books(request):
    books = Books.objects.all()
    return render(request, 'see_books.html', {'books': books})




def update_books(request, id):
    books = Books.objects.get(pk=id)
    if request.method == "POST":
        # books.author_id=request.POST['author'],
        books.name=request.POST['name'],
        books.caption=request.POST['caption']
        books.save()
        books.author.set([request.POST['author']])
        return redirect('see_books')
    return render(request, 'update_books.html', {'books': books,'author': Author.objects.all()})


def delete_books(request, id):
    book = Books.objects.get(pk=id)
    book.delete()
    return redirect('see_books')                                                                                                  



def create_order(request):
    if request.method == "POST":
        order = Order.objects.create(
            username=request.POST["username"],
            phone=request.POST["phone"],
            book_id=request.POST["books"],
            lend_at=request.POST["lend_at"],
            bring_at=request.POST["bring_at"]
            )
        return redirect('see_order')
    return render(request, 'create_order.html', {'books': Books.objects.all(),'order':order})



def see_order(request):
    orders = Order.objects.all()
    return render(request, 'see_orders.html', {'orders': orders})



def update_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.username = request.POST['username']
        order.phone = request.POST['phone']
        order.lend_at = request.POST['lend_at']
        order.bring_at = request.POST['bring_at']
        order.save()
        order.books.set([request.POST['books']])
        return redirect('see_order')
    return render(request, 'update_order.html', {'order': order,'books': Books.objects.all()})



def delete_order(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('see_order')                                                                                                  
