from typing import Any
from django.views.generic import ListView
from django.db.models.manager import BaseManager

from goods.models import Goods
from goods.mixins.goods_mixins import BaseDataMixin
from goods.services import goods_services
from goods_favourite.mixins.favourite_mixins import GetFavouriteGoodsMixin
from pictures.services import picture_services


class AllGoods(BaseDataMixin, GetFavouriteGoodsMixin, ListView):
    template_name = "goods/all_view_goods.html"
    context_object_name = "goods"

    def get_queryset(self):
        return goods_services.get_goods_data()


class ChoiceGoods(BaseDataMixin, GetFavouriteGoodsMixin, ListView):
    template_name = "goods/choice_type_goods.html"
    context_object_name = "choice_type"

    def get_queryset(self) -> BaseManager[Goods]:
        choice_goods = goods_services.get_all_goods_for_name(
            self.kwargs["type_product"]
        )
        return choice_goods


class Product(GetFavouriteGoodsMixin, ListView):
    model = Goods
    template_name = "goods/product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context["product"] = goods_services.get_product(self.kwargs["product_slug"])
        context["pictures"] = picture_services.get_pictures_from_goods_id(
            context["product"].get().id
        )
        return context


class SearchGoods(BaseDataMixin, GetFavouriteGoodsMixin, ListView):
    template_name = "goods/search_goods.html"
    context_object_name = "search_goods"

    
    def get_queryset(self) -> BaseManager[Goods]:
        search_goods = goods_services.get_search_goods(
            self.request.GET.get("search_form")
        )
        return search_goods

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.request.GET.get("search_form")
        return context
