from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from goods.models import Goods, CategoryGoods
from goods import views


class ChoiceGoodsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.max_count_goods_on_page = views.ChoiceGoods.paginate_by
        cat = CategoryGoods.objects.create(name="Верхняя-одежда", slug="cheq")
        Goods.objects.create(
            name="Кардиган", slug="Kardigan", color="pink", main_photo="asdasd", category=cat
        )

    def test_url_status_code(self):
        """The url works correctly when specifying the path"""

        response = self.client.get("/choice_goods/Верхняя-одежда/")

        self.assertEqual(response.status_code, 200)

    def test_url_status_by_name(self):
        """The url works correctly when specifying the namespace"""

        response = self.client.get(
            reverse("choice_goods", kwargs={"type_product": "Верхняя-одежда"})
        )

        self.assertEqual(response.status_code, 200)

    def test_url_status_without_goods(self):
        """The url works correctly without goods"""

        response = self.client.get(
            reverse("choice_goods", kwargs={"type_product": "Нчфыв"})
        )

        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        """The template name is write correct"""

        response = self.client.get("/choice_goods/Шапка/")

        self.assertTemplateUsed(response, "goods/choice_type_goods.html")

    def test_context_object_name(self):
        """The context object name is write correct"""

        views_all_goods = views.ChoiceGoods()
        context_object_name_goods = views_all_goods.context_object_name

        self.assertEqual(context_object_name_goods, "choice_type")

    def test_pagination_on_base_page(self):
        """The pagination is correct"""

        response = self.client.get(
            reverse("choice_goods", kwargs={"type_product": "Кардиган"})
        )

        self.assertFalse(response.context["is_paginated"])

    def test_paginate_on_page(self):
        """The pagination with selected number work is correct"""

        response = self.client.get(
            reverse("choice_goods", kwargs={"type_product": "Пальто"}) + "?page=1"
        )

        self.assertEqual(response.context["is_paginated"], False)

    def test_page_without_goods_with_number_page(self):
        """The pagination with selected number without goods work is correct"""

        response = self.client.get(
            reverse("choice_goods", kwargs={"type_product": "Пальто"}) + "?page=2"
        )

        self.assertEqual(response.status_code, 404)

    def test_get_data_list_in_get_queryset(self):
        """The data from the get queryset is returned correct"""

        request = self.factory.get(
            reverse("choice_goods", kwargs={"type_product": "Верхняя-одежда"})
        )
        category = CategoryGoods.objects.first()
        goods = Goods.objects.filter(category=category.id)
        view_choice_goods = views.ChoiceGoods()
        view_choice_goods.setup(request, type_product="Верхняя-одежда")

        queryset_choice_goods = view_choice_goods.get_queryset()

        self.assertQuerysetEqual(goods, queryset_choice_goods)

    def test_return_empty_list_in_get_queryset(self):
        """There is no data in the database"""

        request = self.factory.get(
            reverse("choice_goods", kwargs={"type_product": "Пальто"})
        )
        goods = Goods.objects.filter(name="Пальто")
        view_choice_goods = views.ChoiceGoods()
        view_choice_goods.setup(request, type_product="Пальто")

        queryset_choice_goods = view_choice_goods.get_queryset()

        self.assertQuerysetEqual(goods, queryset_choice_goods)
