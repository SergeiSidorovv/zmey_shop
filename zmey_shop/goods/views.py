from typing import Any
from django.views.generic import ListView
from django.db.models.manager import BaseManager

from goods.models import Goods
from goods.services import goods_services
from goods_favourite.services import favourite_services


class AllGoods(ListView):
    model = Goods
    template_name = "goods/all_view_goods.html"
    context_object_name = "goods"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["goods"] = goods_services.get_goods_data()
        context["favourite_goods"] = favourite_services.get_favourite_goods_id(
            user_id=self.request.user.id
        )
        return context


class Product(ListView):
    model = Goods
    template_name = "goods/product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["product"] = goods_services.get_product(self)
        return context


class SearchGoods(ListView):
    model = Goods
    template_name = "goods/search_goods.html"
    context_object_name = "search_goods"

    def get_queryset(self) -> BaseManager[Goods]:
        search_goods = goods_services.get_search_goods(
            self.request.GET.get("search_form")
        )
        return search_goods

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.request.GET.get("search_form")
        context["favourite_goods"] = favourite_services.get_favourite_goods_id(
            user_id=self.request.user.id
        )
        return context