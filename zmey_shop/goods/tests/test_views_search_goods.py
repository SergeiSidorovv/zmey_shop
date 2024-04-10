from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from goods import views
from goods.models import Goods


class SearchGoodsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        Goods.objects.create(
            name="Перчатки", slug="Perchatki", color="pink", main_photo="asdasd"
        )

    def test_url_status_code(self):
        """The url works correctly when specifying the path"""

        response = self.client.get("/search/", {"search_form": "Перчатки"})

        self.assertEqual(response.status_code, 200)

    def test_url_status_by_name(self):
        """The url works correctly when specifying the namespace"""

        response = self.client.get(reverse("search"), {"search_form": "Перчатки"})

        self.assertEqual(response.status_code, 200)
    
    def test_url_status_without_data(self):
        """The url works correctly when without data"""

        response = self.client.get(reverse("search"), {})

        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        """The template name is write correct"""

        response = self.client.get(reverse("search"), {"search_form": "Перчатки"})

        self.assertTemplateUsed(response, "goods/search_goods.html")


    def test_name_available_from_search_form(self):
        """The search form works correctly with the name"""

        request = self.factory.get(reverse("search"), {"search_form": "Шнурки"})
        name_search_form = request.GET.get("search_form")
        self.assertEqual(name_search_form, "Шнурки")


    def test_get_data_list_in_get_queryset(self):
        """The data from the get queryset is returned correct"""

        request = self.factory.get("/search/", {"search_form": "Перчатки"})
        products = Goods.objects.filter(name=request.GET.get("search_form"))
        view_search_goods = views.SearchGoods()
        view_search_goods.setup(request)

        queryset_search_goods = view_search_goods.get_queryset()

        self.assertQuerysetEqual(products, queryset_search_goods)

