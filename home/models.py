from django.db import models

# Create your models here.
CATEGORY_CHOICES = {
    ('pd','Papad'),
    ('ck','Cakes'),
    ('pr','PuranPoli'),
}
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    Product_image = models.ImageField(upload_to='Product')

    def __str__(self):
        return self.title

class singup(models.Model):
    first_name = models.CharField(max_length=15)
    medal_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    contact = models.IntegerField()
    birth_date = models.DateField()
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_namename


class about(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone_no = models.IntegerField()
    query = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    