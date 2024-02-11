from django.db import models


class Pictures(models.Model):
    """Pictures models in the database"""

    photo = models.ImageField(upload_to="photo", verbose_name="фото", null=True)
    goods = models.ForeignKey("goods.Goods", models.CASCADE, verbose_name="id_вещи")

    def __str__(self) -> str:
        """Returns the pictures name"""

        return "Фотография"

    class Meta:
        """Metadata by model"""

        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"
        ordering = ["id"]
