from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from goods_favourite.models import Favourite
from goods.models import Goods


class FavouriteModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.request = cls.factory.get("favourite/")

        user = User.objects.create(username="username", password="top_secret")

        product = Goods.objects.create(
            name="Сумка", slug="symka", color="red", main_photo="asdasd"
        )
        Favourite.objects.create(user_id=user.id, goods_id=product.id)

    def test_user_id_label(self):
        """The user id label is written correctly"""

        favourite_product = Favourite.objects.first()
        field_label = favourite_product._meta.get_field("goods_id").verbose_name

        self.assertEqual(field_label, "id_вещи")

    def test_goods_id_label(self):
        """The goods id label is written correctly"""

        favourite_product = Favourite.objects.first()
        field_label = favourite_product._meta.get_field("user_id").verbose_name

        self.assertEqual(field_label, "id_пользователя")

    def test_str_object_name(self):
        """The object is written correctly"""

        favourite_products = Favourite.objects.last()
        str_object_name = str(favourite_products)

        self.assertEqual(str_object_name, "Избранное")

    def test_verbose_name_meta(self):
        """The verbose name in meta written is correct"""

        favourite_product = Favourite.objects.last()
        verbose_name_favourite = favourite_product._meta.verbose_name

        self.assertEqual(verbose_name_favourite, "Избранное")

    def test_verbose_name_plural_meta(self):
        """The verbose name plural in meta written is correct"""

        favourite_product = Favourite.objects.first()
        verbose_name_plural_favourite = favourite_product._meta.verbose_name_plural

        self.assertEqual(verbose_name_plural_favourite, "Избранные")

    def test_ordering_meta(self):
        """The ordering in meta written is correct"""

        favourite_product = Favourite.objects.first()
        ordering_favourite = favourite_product._meta.ordering

        self.assertEqual(ordering_favourite, ["id"])
