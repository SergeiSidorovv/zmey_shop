from typing import Any
from django.views.generic import ListView

from goods.models import Goods
from goods.services import goods_services


class AllGoods(ListView):
    model = Goods
    template_name = "goods/all_view_goods.html"
    context_object_name = "goods"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["goods"] = goods_services.get_goods_data()
        return context


class Product(ListView):
    model = Goods
    template_name = "goods/product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["product"] = goods_services.get_product(self)
        return context
        