from django.test import TestCase
from django.template import Template, Context
from django import template

from goods.templatetags import goods_tags
from goods.services import goods_services
from goods.models import Goods


class GoodsTagsTest(TestCase):

    TEMPLATE = Template("{% load goods_tags %} {% get_types_goods %}")

    def setUp(self) -> None:
        Goods.objects.create(
            name="Сумка", slug="symka", color="red", main_photo="asdasd"
        )
        Goods.objects.create(
            name="Шапка", slug="shapka", color="red", main_photo="asdasd"
        )

    def test_tempplate_in_get_types_goods(self):
        rendered = self.TEMPLATE.render(Context({}))
        template_types_goods = '<a href="/choice_goods/%D0%A1%D1%83%D0%BC%D0%BA%D0%B0/"> Сумка </a>\
                    <a href="/choice_goods/%D0%A8%D0%B0%D0%BF%D0%BA%D0%B0/"> Шапка </a>'

        self.assertInHTML(template_types_goods,rendered)

    def test_get_data_get_types_goods(self):
        types_goods = goods_tags.get_types_goods()
        test_type_goods = {"types_goods": goods_services.get_all_names_goods()}

        self.assertQuerysetEqual(types_goods, test_type_goods)
