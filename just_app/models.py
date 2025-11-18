from django.db import models

class Author(models.Model):
    name = models.CharField('Имя')

class Publisher(models.Model):
    name = models.CharField('Название издательства')

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField('Название')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


# class Manufacturer(models.Model):
#     name = models.CharField()

# class Item(models.Model):
#     name = models.CharField()
#     price = models.DecimalField()
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=CASCADE)
#     quantity = models.IntegerField()
