from django.db.models.manager import BaseManager

from pictures.models import Pictures


def get_pictures_from_goods_id(product_id: int) -> BaseManager[Pictures]:
    """Gives pictures from the databse table by product id

    Keyword arguments:
    product_id -- a parameter that transmits a uniqe product id"""
    pictures = Pictures.objects.filter(goods_id=product_id).only("id", "photo")
    return pictures
