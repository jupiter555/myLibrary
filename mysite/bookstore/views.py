from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import BookStore,Book,Author
import time
# Create your views here.

def add_book(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        # 录入数据
        title = request.POST.get('title')
        if not title:
            return HttpResponse('书名数据有误 请退出重写')
        pub = request.POST.get('pub')
        if not pub:
            return HttpResponse('出版社数据有误 请退出重写')
        price = request.POST.get('price')
        if not price:
            return HttpResponse('定价数据有误 请退出重写')
        market_price = request.POST.get('m_price')
        if not market_price:
            return HttpResponse('零售价数据有误 请退出重写')

        # 创建数据
        Book.objects.create(title=title, pub=pub, price=price, market_price=market_price)


        return HttpResponseRedirect('/bookstore/all_book')

def add_author(request):
    if request.method == 'GET':
        return render(request,'bookstore/add_author.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        if not name:
            return HttpResponse('姓名数据有误 请退出重写')
        age = request.POST.get('age')
        if not age:
            return HttpResponse('姓名数据有误 请退出重写')
        email = request.POST.get('email')
        if not email:
            return HttpResponse('姓名数据有误 请退出重写')

        # 创建数据
        Author.objects.create(name=name,age=age,email=email)
        return HttpResponse('作者信息添加成功')

def all_book(request):
    #获取所有书籍
    all_book = Book.objects.all()
    return render(request,'bookstore/all_book.html',locals())

def detail(request,book_id):
    #书籍详情页面
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        return HttpResponse('您当前查阅的书籍有误,请重新查询')

    return render(request,'bookstore/detail.html',locals())

def update_book(request,book_id):
    #1.查
    books = Book.objects.filter(id=book_id)
    if not books:
        return HttpResponse('当前查阅书籍有误')
    if request.method != 'POST':
        return HttpResponse('当前请求异常')

    market_price = request.POST.get('m_price')
    book = books[0]
    #2.赋值
    book.market_price = market_price
    #3.存储
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')

def delete_book(request,book_id):
    #删除书籍
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
    except Exception as e:
        return HttpResponse('您提交的数据有误,请您刷新页面后重试')
    return HttpResponseRedirect('/bookstore/all_book    ')


