from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from goods.models import Goods
from goods import views


class AllGoodsViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.max_count_goods_on_page = views.AllGoods.paginate_by
        count_goods = 16
        for _ in range(count_goods):
            Goods.objects.create(
                name="пальто", slug=f"palto{_}", color="pink", main_photo="asdasd"
            )

    def test_url_status_code(self):
        """The url works correctly when specifying the path"""

        response = self.client.get("")

        self.assertEqual(response.status_code, 200)

    def test_url_status_by_name(self):
        """The url works correctly when specifying the namespace"""

        response = self.client.get(reverse("goods"))

        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        """The template name is write correct"""

        response = self.client.get("")

        self.assertTemplateUsed(response, "goods/all_view_goods.html")

    def test_context_object_name(self):
        """The context object name is write correct"""

        views_all_goods = views.AllGoods()
        context_object_name_goods = views_all_goods.context_object_name

        self.assertEqual(context_object_name_goods, "goods")

    def test_pagination_on_base_page(self):
        """The pagination is correct"""

        response = self.client.get(reverse("goods"))

        self.assertTrue(response.context["is_paginated"])

    def test_paginate_on_page(self):
        """The pagination with selected number work is correct"""

        response = self.client.get(reverse("goods") + "?page=1")

        self.assertEqual(response.context["is_paginated"], True)
        

    def test_get_data_in_get_queryset(self):
        """The product data is given correctly"""

        request = self.factory.get("")
        goods = Goods.objects.all()
        view_all_goods = views.AllGoods()
        view_all_goods.setup(request)

        queryset_all_goods = view_all_goods.get_queryset()

        self.assertQuerysetEqual(goods, queryset_all_goods)
