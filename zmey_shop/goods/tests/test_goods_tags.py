from django.test import TestCase
from django.template import Template, Context

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
        template_types_goods = ''

        self.assertInHTML(template_types_goods, rendered)

    def test_get_data_get_types_goods(self):
        types_goods = goods_tags.get_types_goods()
        test_type_goods = {"types_goods": goods_services.get_all_category_name()}

        self.assertQuerysetEqual(types_goods, test_type_goods)
