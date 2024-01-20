from django.test import TestCase
from django.db.models import QuerySet

from pictures.services import picture_services
from pictures.models import Pictures
from goods.models import Goods


class PictureServicesTest(TestCase):
    def setUp(self):
        product = Goods.objects.create(
            name="кардиган", slug="kardigan", color="pink", main_photo="asdasd"
        )
        second_product = Goods.objects.create(
            name="шапка", slug="shapka", color="red", main_photo="asdasd"
        )
        Pictures.objects.create(photo="IMG_R_0067.jpg", goods_id=product.id)
        Pictures.objects.create(
            photo="photo_2023-11-19_19-04-03.jpg", goods_id=product.id
        )
        Pictures.objects.create(photo="IMG_R_0067.jpg", goods_id=second_product.id)

    def test_count_get_pictures_from_goods_id(self):
        """The number of photos for the product is calculated correctly"""

        product_id = Goods.objects.get(slug="kardigan").id
        pictures_data_queryset = Pictures.objects.filter(goods_id=product_id)
        pictures = picture_services.get_pictures_from_goods_id(product_id=product_id)

        self.assertEqual(len(pictures), len(pictures_data_queryset))

    def test_type_get_data_from_get_pictures(self):
        """The type of data returned is specifed correctly"""

        product_id = Goods.objects.get(slug="shapka").id
        pictures = picture_services.get_pictures_from_goods_id(product_id)

        self.assertEqual(type(pictures), QuerySet)

    def test_type_pictures_from_get_pictures(self):
        """The type of pictures returned is specifed correctly"""

        product_id = Goods.objects.get(slug="kardigan").id
        pictures = picture_services.get_pictures_from_goods_id(product_id)

        self.assertEqual(type(pictures.first()), Pictures)

    def test_get_none_data_from_get_pictures(self):
        """When passing an invalid id product"""

        pictures = picture_services.get_pictures_from_goods_id(-15)

        self.assertEqual(pictures.first(), None)
