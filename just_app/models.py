from django.db import models

class Product(models.Model):
    name = models.CharField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    article = models.IntegerField("Article", primary_key=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"

class Size(models.Model):
    ST = [
        ("S" , "S"),
        ("M", "M"),
        ("L", "L")
    ]
    art_product = models.ManyToManyField(Product, verbose_name='Product')
    size = models.CharField('Size', max_length=2, choices=ST)
    
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return f"{self.art_product}"
