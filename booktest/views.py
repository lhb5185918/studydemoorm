from django.shortcuts import render
from django.shortcuts import HttpResponse
from booktest.models import Book,Publish,Author,AuthorDetail
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.



@csrf_exempt
def add(reqquest):
    #一对多
    # book = Book.objects.create(title="三国演绎",price=100,publishDate="1986-01-01",publish = Publish.objects.get(id =1))
    # book.authors.add(1,2)
    # book = Book.objects.create(title="红楼梦",price=99,publishDate="1986-03-01",publish_id = 2)
    # print(book.publish.name)
    #一对一的添加
    # Author.objects.create(name="张志忠",age=20,ad_id = 3, id =2)
    #多对多的添加
    # bookauth = Book.objects.get(id =1)
    # bookauth.authors.add()
    #简化写法
    # book = Book.objects.get(id = 1)
    # book.authors.add(1,3)
    #多对多的删除
    # book.authors.remove(1)
    # book.authors.clear()
    # book.authors.set([1,2])
    #关系表的查询
    # book = Book.objects.get(title = "三国演绎")
    # result = book.authors.all().values('name')
    # book = Author.objects.get(name = "曹雪芹")
    # result = book.books.all().values('title')
    # print(result)
    publish = Publish.objects.get(name = "苹果出版社")
    result = publish.books_list.all().values('title')
    print(result)





    return HttpResponse("添加成功")




@csrf_exempt

def index(request):
    booke_list = Book.objects.all()
    print(booke_list.values("publishDate"))

    return render(request,"index.html",{"books": booke_list})


@csrf_exempt
def addbook(request):
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request,"addbook.html",{"publishes":publish_list,"authors":author_list})