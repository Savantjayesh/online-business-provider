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
    