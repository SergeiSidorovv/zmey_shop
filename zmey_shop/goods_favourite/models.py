from django.db import models


class Favourite(models.Model):
    user = models.ForeignKey(
        "auth.User", models.CASCADE, verbose_name="id_пользователя"
    )
    goods = models.ForeignKey("goods.Goods", models.CASCADE, verbose_name="id_вещи")

    def __str__(self) -> str:
        return "Избранное"

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        ordering = ["id"]
