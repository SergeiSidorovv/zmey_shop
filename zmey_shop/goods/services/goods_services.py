from django.db.models.manager import BaseManager

from goods.models import Goods


def get_goods_data() -> BaseManager[Goods]:
    """Получает из таблицы Goods всю информацию по всем вещам и возвращает её"""

    goods_data = Goods.objects.all()
    return goods_data

def get_product(self) -> BaseManager[Goods]:
    """gives away the product

    Keyword arguments:
    self -- a reference to the current instance of the class
    """

    product = Goods.objects.filter(slug=self.kwargs["product_slug"])
    return product