from django.test import TestCase

from goods.models import Goods
from goods.mixins import goods_mixins


class BaseDataMixinTest(TestCase):
    def test_model_mixin(self):
        """The model from mixin is correct"""

        model_mixin = goods_mixins.BaseDataMixin.model

        self.assertEqual(model_mixin, Goods)

    def test_paginate_by_mixin(self):
        """The paginate from mixin is correct"""

        paginate_mixin = goods_mixins.BaseDataMixin.paginate_by

        self.assertEqual(paginate_mixin, 15)
