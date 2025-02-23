from django.db import models
from django.db.models import SlugField
from django.utils.timezone import now


# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)  #بشه slug
    name = models.CharField(max_length=50)  #برای نوشتن روی ویدیو
    titr = models.TextField(max_length=100, default="")
    sub_titr = models.CharField(max_length=150, blank=True)
    about_machine = models.TextField(default="")
    image_1 = models.FileField(upload_to="media", null=True, blank=True)
    tarahi_zaheri = models.TextField(default="", null=True, blank=True)
    image_2 = models.FileField(upload_to="media", null=True, blank=True)
    moshakhasat_fanni = models.TextField(default="", null=True, blank=True)
    image_3 = models.FileField(upload_to="media", null=True, blank=True)
    tarahi_dakheli = models.TextField(default="", null=True, blank=True)
    image_4 = models.FileField(upload_to="media", null=True, blank=True)
    mazaya = models.TextField(default="", null=True, blank=True)
    image_5 = models.FileField(upload_to="media", null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = SlugField(default="", null=True, unique=True, db_index=True)
    embed_code = models.TextField(default="", null=True, blank=True)
    hashtag1 = models.CharField(max_length=50, default="", null=True, blank=True)
    hashtag2 = models.CharField(max_length=50, default="", null=True, blank=True)

    def __str__(self):
        return self.name


class CarSpecs(models.Model):
    review = models.OneToOneField('Review', on_delete=models.CASCADE, related_name='specs')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50)
    production_year = models.PositiveIntegerField(null=True, blank=True)
    engine_capacity = models.PositiveIntegerField(null=True, blank=True)
    cylinders = models.PositiveIntegerField(null=True, blank=True)
    valve = models.PositiveIntegerField(null=True, blank=True)
    tanafos = models.PositiveIntegerField(null=True, blank=True)
    torque = models.PositiveIntegerField(null=True, blank=True)
    hp = models.PositiveIntegerField(null=True, blank=True)
    max_speed = models.PositiveIntegerField(null=True, blank=True)
    sefr_sad = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=1)
    gearbox = models.CharField(max_length=50, null=True, blank=True)
    differential = models.CharField(max_length=50, null=True, blank=True)
    talig_jolo = models.CharField(max_length=50, null=True, blank=True)
    talig_agab = models.CharField(max_length=50, null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    fuel_tank = models.PositiveIntegerField(null=True, blank=True)
    masraf_sokht = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=1)
    ring = models.CharField(max_length=50, null=True, blank=True)
    mother_brand = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)


class Khabar(models.Model):
    title = models.CharField(max_length=50)  #بشه slug
    titr = models.TextField(max_length=100, default="")
    image = models.FileField(upload_to="media", null=True, blank=True)
    sub_titr = models.TextField(max_length=1000, default="")
    mozo1 = models.TextField(max_length=100, default="", null=True, blank=True)  #بشه سرتیتر
    sub_mozo1 = models.TextField(max_length=1000, default="", null=True, blank=True)  #بشه متن تیتر
    image_1 = models.FileField(upload_to="media", null=True, blank=True)
    mozo2 = models.TextField(max_length=100, default="", null=True, blank=True)
    sub_mozo2 = models.TextField(max_length=1000, default="", null=True, blank=True)
    image_2 = models.FileField(upload_to="media", null=True, blank=True)
    mozo3 = models.TextField(max_length=100, default="", null=True, blank=True)
    sub_mozo3 = models.TextField(max_length=1000, default="", null=True, blank=True)
    image_3 = models.FileField(upload_to="media", null=True, blank=True)
    mozo4 = models.TextField(max_length=100, default="", null=True, blank=True)
    sub_mozo4 = models.TextField(max_length=1000, default="", null=True, blank=True)
    image_4 = models.FileField(upload_to="media", null=True, blank=True)
    image_5 = models.FileField(upload_to="media", null=True, blank=True)
    image_6 = models.FileField(upload_to="media", null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    slug = SlugField(default="", null=True, unique=True, db_index=True)
    hashtag1 = models.CharField(max_length=50, default="", null=True, blank=True)
    hashtag2 = models.CharField(max_length=50, default="", null=True, blank=True)

    def __str__(self):
        return self.titr


class DailyPageView(models.Model):
    page_name = models.CharField(max_length=250)
    views_count = models.PositiveIntegerField(default=0)
    date = models.DateField(default=now())

    class Meta:
        unique_together = ('page_name', 'date')

    def __str__(self):
        return f"{self.page_name} - {self.date}:{self.views_count}"
