from django.db import models
from django.urls import reverse


class Goods(models.Model):
    name = models.CharField(max_length=60, verbose_name="Имя")
    slug = models.SlugField(max_length=60, unique=True, verbose_name="URL")
    article = models.IntegerField(unique=True, null=True, verbose_name="Артикль")
    description = models.TextField(
        max_length=5000, null=True, verbose_name="Описание товара"
    )
    yarn = models.CharField(max_length=100, null=True, verbose_name="Название пряжи")
    composition = models.CharField(max_length=100, null=True, verbose_name="Состав")
    additional_materials = models.CharField(
        max_length=100, null=True, verbose_name="Доп. материалы"
    )
    color = models.CharField(max_length=60, verbose_name="Цвет")
    main_photo = models.ImageField(
        upload_to="main_photo", null=True, verbose_name="Основное_фото"
    )
    category = models.ForeignKey(
        "CategoryGoods", on_delete=models.PROTECT, null=True, verbose_name="категории"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"product_slug": self.slug})

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"
        indexes = [models.Index(fields=["slug"])]
        ordering = ["id"]


class CategoryGoods(models.Model):
    name = models.CharField(max_length=60, verbose_name="Категория")
    slug = models.SlugField(max_length=60, unique=True, verbose_name="URL-категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]
