from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse

from goods_favourite import views
from goods_favourite.models import Favourite
from goods.models import Goods


class FavouriteGoodsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.paginate = views.FavouriteGoods.paginate_by
        self.model = views.FavouriteGoods.model

        user = User.objects.create_user(username="username", password="top_secret")
        product = Goods.objects.create(
            name="Шарф", slug="sharf", color="red", main_photo="asdasd"
        )
        Favourite.objects.create(user_id=user.id, goods_id=product.id)

    def test_url_status_code_without_register(self):
        """The url works correctly without register user when specifying the path"""

        response = self.client.get("/favourite/")

        self.assertEqual(response.status_code, 302)

    def test_url_status_code_with_register(self):
        """The url works correctly with register user when specifying the path"""

        self.client.login(username="username", password="top_secret")
        response = self.client.get("/favourite/")

        self.assertEqual(response.status_code, 200)

    def test_url_status_by_name_with_register(self):
        """The url works correctly when specifying the namespace"""

        self.client.login(username="username", password="top_secret")
        response = self.client.get(reverse("favourite:favourite_goods"))

        self.assertEqual(response.status_code, 200)

    def test_url_status_by_name_without_register(self):
        """The url works correctly when specifying the namespace"""

        response = self.client.get(reverse("favourite:favourite_goods"))

        self.assertEqual(response.status_code, 302)

    def test_count_product_on_page(self):
        """The count produtc displayed on page is correct"""

        self.assertEqual(self.paginate, 15)

    def test_type_model(self):
        """The model use in view is correct"""

        self.assertEqual(self.model, Favourite)

    def test_template_name(self):
        """The template name is write correct"""

        self.client.login(username="username", password="top_secret")
        response = self.client.get("/favourite/")

        self.assertTemplateUsed(response, "goods_favourite/favourite_goods_view.html")

    def test_context_object_name(self):
        """The context object name is write correct"""

        views_favourite = views.FavouriteGoods()
        context_object_name_favourite = views_favourite.context_object_name

        self.assertEqual(context_object_name_favourite, "favourites")

    def test_get_queryset(self):
        """The function return queryset is correct"""

        self.client.login(username="username", password="top_secret")
        request = self.factory.get(reverse("favourite:favourite_goods"))
        request.user = User.objects.get(username="username")
        view_favourite_goods = views.FavouriteGoods()
        view_favourite_goods.setup(request)

        user_id = request.user.id
        favourite_goods = Favourite.objects.filter(user_id=user_id)
        query_set_favourite_goods = view_favourite_goods.get_queryset()

        self.assertQuerysetEqual(query_set_favourite_goods, favourite_goods)
