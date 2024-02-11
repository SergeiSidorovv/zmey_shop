from django.db import models


class Favourite(models.Model):
    """Favourite models in the database"""

    user = models.ForeignKey(
        "auth.User", models.CASCADE, verbose_name="id_пользователя"
    )
    goods = models.ForeignKey("goods.Goods", models.CASCADE, verbose_name="id_вещи")

    def __str__(self) -> str:
        """Returns the favourite name"""

        return "Избранное"

    class Meta:
        """Metadata by model"""
        
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        ordering = ["id"]
