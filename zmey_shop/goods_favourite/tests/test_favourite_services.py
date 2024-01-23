from django.test import TestCase
from django.contrib.auth.models import User

from goods_favourite.services import favourite_services
from goods_favourite.models import Favourite
from goods.models import Goods


class FavouriteServicesTest(TestCase):
    def setUp(self):
        self.product = Goods.objects.create(
            name="кардиган", slug="kardigan", color="pink", main_photo="asdasd"
        )
        self.product_2 = Goods.objects.create(
            name="Шапка", slug="Shapka", color="red", main_photo="IMG_R_0067.JPG"
        )
        self.user = User.objects.create_user(username="username", password="top_secret")
        self.user_2 = User.objects.create_user(
            username="username2", password="top_secret2"
        )
        Favourite.objects.create(user_id=self.user.id, goods_id=self.product.id)
        Favourite.objects.create(user_id=self.user.id, goods_id=self.product_2.id)
        Favourite.objects.create(user_id=self.user_2.id, goods_id=self.product_2.id)

    def test_get_favourite_goods(self):
        """The function with user id returned is correct favourite goods"""

        favourite_goods_test = Favourite.objects.filter(
            user_id=self.user
        ).select_related("goods")
        favourite_goods = favourite_services.get_favourite_goods(self.user.id)

        self.assertQuerysetEqual(favourite_goods, favourite_goods_test)

    def test_get_favourite_product(self):
        """The function with user id and id product returned is correct favourite product"""

        favourite_goods_test = Favourite.objects.filter(
            user_id=self.user_2, goods_id=self.product_2
        ).select_related("goods")
        favourite_goods = favourite_services.get_favourite_product(
            self.user_2, self.product_2
        )

        self.assertQuerysetEqual(favourite_goods, favourite_goods_test)

    def test_create_product_in_favourite(self):
        """The function creates a favourite product in the database."""

        favourite_services.create_product_in_favourite(self.user_2.id, self.product.id)
        count_favourite_goods_user = Favourite.objects.filter(
            user_id=self.user_2.id
        ).count()
        self.assertEqual(count_favourite_goods_user, 2)

    def test_favourite_goods_id(self):
        """The function with user id returned is correct favourite goods id"""

        favourite_goods_id_test = Favourite.objects.filter(
            user_id=self.user.id
        ).values_list("goods_id", flat=True)

        favourite_goods_id = favourite_services.get_favourite_goods_id(self.user.id)

        self.assertQuerysetEqual(favourite_goods_id, favourite_goods_id_test)

    def test_delete_favourite_product(self):
        """The function is correct delete favourite product from database"""

        favourite_services.delete_favourite_product(self.product)
        count_favourite_goods = Favourite.objects.all().count()

        self.assertEqual(count_favourite_goods, 2)
