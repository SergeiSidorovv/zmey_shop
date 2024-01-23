from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse

from goods_favourite import views
from goods_favourite.models import Favourite
from goods.models import Goods


class ManagefavouriteGoodsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        product = Goods.objects.create(
            name="кардиган", slug="kardigan", color="pink", main_photo="asdasd"
        )
        Goods.objects.create(
            name="Шапка", slug="Shapka", color="red", main_photo="IMG_R_0067.JPG"
        )
        user = User.objects.create_user(username="username", password="top_secret")
        Favourite.objects.create(user_id=user.id, goods_id=product.id)

    def test_url_status_code(self):
        """The url works correctly when specifying the path"""

        product_id = Goods.objects.first().id
        self.client.login(username="username", password="top_secret")

        response = self.client.post(
            f"/favourite/{product_id}", HTTP_REFERER="http://127.0.0.1:8000/"
        )

        self.assertEqual(response.status_code, 302)

    def test_url_status_by_name(self):
        """The url works correctly when specifying the namespace"""

        product_id = Goods.objects.last().id
        self.client.login(username="username", password="top_secret")

        response = self.client.post(
            reverse("favourite:add", kwargs={"id_product": product_id}),
            HTTP_REFERER="http://127.0.0.1:8000/favourite/",
        )

        self.assertEqual(response.status_code, 302)

    def test_url_status_without_user(self):
        """The url works correctly when without user"""

        product_id = Goods.objects.last().id

        response = self.client.post(
            reverse("favourite:add", kwargs={"id_product": product_id}),
            HTTP_REFERER="http://127.0.0.1:8000/favourite/",
        )

        self.assertEqual(response.status_code, 302)

    def test_post_without_user(self):
        """The count favourites goods dont changes in database"""

        product_id = Goods.objects.get(slug="kardigan").id
        request = self.factory.post(
            f"/favourite/{product_id}", HTTP_REFERER="http://127.0.0.1:8000/"
        )
        request.user = AnonymousUser()
        view_manage_favourite = views.ManageFavouriteGoods()
        view_manage_favourite.setup(request)

        view_manage_favourite.post(request, product_id)
        count_favourite_goods = len(Favourite.objects.all())

        self.assertEqual(count_favourite_goods, 1)

    def test_delete_product_in_db_through_post(self):
        """The count favourites goods decreased in database"""

        product_id = Goods.objects.get(slug="kardigan").id
        request = self.factory.post(
            f"/favourite/{product_id}", HTTP_REFERER="http://127.0.0.1:8000/favourite"
        )
        request.user = User.objects.get(username="username")
        view_manage_favourite = views.ManageFavouriteGoods()
        view_manage_favourite.setup(request)

        view_manage_favourite.post(request, product_id)
        count_favourite_goods = len(Favourite.objects.all())

        self.assertEqual(count_favourite_goods, 0)

    def test_add_product_in_db_through_post(self):
        """The count favourites goods added in database"""

        product_id = Goods.objects.get(slug="Shapka").id
        request = self.factory.post(
            f"/favourite/{product_id}", HTTP_REFERER="http://127.0.0.1:8000/favourite"
        )
        request.user = User.objects.get(username="username")
        view_manage_favourite = views.ManageFavouriteGoods()
        view_manage_favourite.setup(request)

        view_manage_favourite.post(request, product_id)
        count_favourite_goods = Favourite.objects.all().count()

        self.assertEqual(count_favourite_goods, 2)
