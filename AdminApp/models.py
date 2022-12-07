from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cat_name

    class Meta:
        db_table = "Category"

class Cake(models.Model):
    cname = models.CharField(max_length=20)
    cake_image = models.ImageField(default="abc.jpg",upload_to="images")
    price = models.FloatField(default=100)
    description = models.CharField(max_length=20)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = "Cake"
