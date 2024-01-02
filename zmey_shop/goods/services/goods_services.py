from django.db.models.manager import BaseManager
from django.db.models import Count

from goods.models import Goods


def get_goods_data() -> BaseManager[Goods]:
    """Get goods all data from database"""

    goods_data = Goods.objects.all()
    return goods_data


def get_product(self) -> BaseManager[Goods]:
    """Gives away the product

    Keyword arguments:
    self -- a reference to the current instance of the class
    """

    product = Goods.objects.filter(slug=self.kwargs["product_slug"])
    return product


def get_all_goods_for_name(name) -> BaseManager[Goods]:
    """Gives all products from the database that have the same names as the name parameter

    Keyword arguments:
    name -- a parameter that transmits the product name
    """

    choice_goods = Goods.objects.filter(name=name)
    return choice_goods


def get_all_names_goods() -> BaseManager[Goods]:
    """Gives away all types goods"""

    names_goods = Goods.objects.order_by('name').distinct('name')
    return names_goods


def get_search_goods(name_product: BaseManager[Goods]) -> BaseManager[Goods]:
    """Get all data about goods by search name product from Goods database

    Keyword arguments:
    name_product -- criteria for searching products with a similar name in Goods database
    """

    search_goods = Goods.objects.filter(name__icontains=name_product)
    return search_goods
