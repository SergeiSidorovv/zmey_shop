from django.db.models.manager import BaseManager

from goods.models import Goods


def get_goods_data() -> BaseManager[Goods]:
    """Get goods all data from database"""

    goods_data = Goods.objects.all()
    return goods_data


def get_product(self) -> BaseManager[Goods]:
    """gives away the product

    Keyword arguments:
    self -- a reference to the current instance of the class
    """

    product = Goods.objects.filter(slug=self.kwargs["product_slug"])
    return product


def get_all_name() -> BaseManager[Goods]:
    """gives away all categories"""

    categories = Goods.objects.get()
    return categories
