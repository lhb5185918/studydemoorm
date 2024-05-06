from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publishDate = models.DateField()

    #一对多关联字段，创建关联字段
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE,related_name="books_list")

    #多对多关联字段，创建关系表
    authors = models.ManyToManyField("Author",db_table="Author2Book",related_name="books")#生成关系表的名字是book_authors



class Publish(models.Model):
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=200)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    #一对一关联字段，创建关联字段
    ad = models.OneToOneField("AuthorDetail" , on_delete=models.CASCADE)


# class Author2Book(models.Model):
#     models.ForeignKey("Book",on_delete=models.CASCADE)
#     models.ForeignKey("Author",on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=200)

