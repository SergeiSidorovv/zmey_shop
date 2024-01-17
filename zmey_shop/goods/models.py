from django.db import models
from django.urls import reverse


class Goods(models.Model):
    name = models.CharField(max_length=60, verbose_name="имя")
    slug = models.SlugField(max_length=60, unique=True, verbose_name="URL")
    color = models.CharField(max_length=60, verbose_name="цвет")
    main_photo = models.ImageField(upload_to='main_photo', verbose_name='основное_фото', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"product_slug": self.slug})

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"
        indexes = [models.Index(fields=["slug"])]
        ordering = ["id"]
