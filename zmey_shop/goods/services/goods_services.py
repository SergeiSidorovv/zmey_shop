from django.db.models.manager import BaseManager

from goods.models import Goods, CategoryGoods


def get_goods_data() -> BaseManager[Goods]:
    """Get goods all data from database"""

    goods_data = Goods.objects.all()
    return goods_data


def get_product(slug: str) -> BaseManager[Goods]:
    """Gives away the product

    Keyword arguments:
    slug -- a parameter that transmits the product slug
    """

    product = Goods.objects.filter(slug=slug)
    return product


def get_all_goods_for_category(category: str) -> BaseManager[Goods] | str:
    """Gives all products from the database that have the same names as the name parameter

    Keyword arguments:
    name -- a parameter that transmits the product name
    """

    category = CategoryGoods.objects.filter(name=category)
    if category:
        category_id = category.get().id
        choice_goods = Goods.objects.filter(category=category_id)
        return choice_goods
    return category

def get_all_category_name() -> BaseManager[Goods]:
    """Gives away all types goods"""

    names_goods = CategoryGoods.objects.order_by("name").distinct("name")
    return names_goods


def get_search_goods(name_product: BaseManager[Goods]) -> BaseManager[Goods]:
    """Get all data about goods by search name product from Goods database

    Keyword arguments:
    name_product -- criteria for searching products with a similar name in Goods database
    """

    search_goods = Goods.objects.filter(name__icontains=name_product)
    return search_goods
