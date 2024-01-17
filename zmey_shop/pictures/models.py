from django.db import models


class Pictures(models.Model):
    photo = models.ImageField(upload_to="photo", verbose_name="фото", null=True)
    goods = models.ForeignKey("goods.Goods", models.CASCADE, verbose_name="id_вещи")

    def __str__(self) -> str:
        return "Фотография"

    class Meta:
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"
        ordering = ["id"]
