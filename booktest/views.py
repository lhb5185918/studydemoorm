from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
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
    if request.method == 'GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,"addbook.html",{"publishes":publish_list,"authors":author_list})
    else:
        print(request.POST)
        # title = request.POST.get("title")
        # price = request.POST.get("price")
        # pubDate = request.POST.get("pubDate")
        # publish_id= request.POST.get("publish_id")
        # authors = request.POST.getlist("author_id")
        data  = request.POST.dict()
        data.pop("author_id")
        print(data)
        authors = request.POST.getlist("author_id")
        book = Book.objects.create(**data)
        #绑定多对多关系
        book.authors.add(*authors)

        return redirect("/index/")

@csrf_exempt
def deletebook(request,detele_id):
    if request.method == "GET":
        return render(request,"deletebook.html")
    else:
        Book.objects.get(id = detele_id).delete()
        return redirect("/index/")

@csrf_exempt
def editpage(request,edit_id):
    if request.method =="GET":
        book = Book.objects.get(id=edit_id)
        print(book.title)
        print(book.publishDate)
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,"editpage.html",{"editbook": book,"publishes":publish_list,"authors":author_list})
    else:
        data = request.POST.dict()
        data.pop("author_id")
        print(data)
        authors = request.POST.getlist("author_id")
        book = (Book.objects.all().filter(id = edit_id).update(**data))
        bookid = Book.objects.get(id = edit_id)
        bookid.authors.set([*authors])
        return redirect("/index/")
