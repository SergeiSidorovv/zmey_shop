from django.db.models.manager import BaseManager

from goods_favourite.models import Favourite


def get_favourite_goods(user_id: int) -> BaseManager[Favourite]:
    """Gives away all the selected favourite products.

    Keyword arguments:
    user_id -- the ID of the registered user
    """

    favourite_goods = Favourite.objects.filter(user_id=user_id).select_related("goods")
    return favourite_goods


def get_favourite_product(user_id: int, id_product: int) -> BaseManager[Favourite]:
    """Gives the selected favourite product.

    Keyword arguments:
    user_id -- the ID of the registered user
    id_product -- the ID of the product
    """

    favourite_product = Favourite.objects.filter(user_id=user_id, goods_id=id_product)
    return favourite_product


def create_product_in_favourite(user_id: int, id_product: int):
    """Product add in Favourite database table

    Keyword arguments:
    user_id -- the ID of the registered user
    id_product -- the ID of the product
    """
    product = Favourite.objects.create(user_id=user_id, goods_id=id_product)
    product.save()


def get_favourite_goods_id(user_id: int) -> BaseManager[Favourite]:
    """Get all ID favourite goods from Favourite database table

    Keyword arguments:
    user_id -- the ID of the registered user
    """

    favourite_goods_id = Favourite.objects.filter(user_id=user_id).values_list(
        "goods_id", flat=True
    )
    return favourite_goods_id


def delete_favourite_product(favourite_product: BaseManager[Favourite]):
    """Favourite product delete from Favourite database"""

    favourite_product.delete()
