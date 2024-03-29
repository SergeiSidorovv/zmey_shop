import logging
from typing import Any
from django.views.generic import ListView
from django.db.models.manager import BaseManager
from django.http import Http404


from goods.models import Goods
from goods.mixins.goods_mixins import BaseDataMixin
from goods.services import goods_services
from goods_favourite.mixins.favourite_mixins import GetFavouriteGoodsMixin
from pictures.services import picture_services


logger = logging.getLogger("django")


class AllGoods(BaseDataMixin, GetFavouriteGoodsMixin, ListView):
    """Transfers all products from the database to the template page"""

    template_name = "goods/all_view_goods.html"
    context_object_name = "goods"

    def get_queryset(self) -> BaseManager[Goods]:
        """Returns the list of items Goods model from database for this view."""

        return goods_services.get_goods_data()


class ChoiceGoods(BaseDataMixin, GetFavouriteGoodsMixin, ListView):
    """
    Transfers all products with the selected type from the database to the template page
    """

    template_name = "goods/choice_type_goods.html"
    context_object_name = "choice_type"

    def get_queryset(self) -> BaseManager[Goods]:
        """
        Returns the list of items Goods model with selected type product from database
        for this view.
        """

        choice_goods = goods_services.get_all_goods_for_category(
            self.kwargs["type_product"]
        )
        return choice_goods


class Product(GetFavouriteGoodsMixin, ListView):
    """Transfers product and pictures product from the database to the template page"""

    model = Goods
    template_name = "goods/product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """
        Returns the dict of item from Goods model with selected slug product,
        and pictures to the item, from database for this view.
        """

        context = super().get_context_data(**kwargs)
        context["product"] = goods_services.get_product(self.kwargs["product_slug"])
        if not context["product"]:
            logger.info("Такокго товара нет, страница не найдена")
            raise Http404()
        context["pictures"] = picture_services.get_pictures_from_goods_id(
            context["product"].get().id
        )
        return context


class SearchGoods(BaseDataMixin, GetFavouriteGoodsMixin, ListView):
    """
    Transfers all products with the selected name from the database to the template page
    """

    template_name = "goods/search_goods.html"
    context_object_name = "search_goods"

    def get_queryset(self) -> BaseManager[Goods]:
        """
        Returns the list of items Goods model with selected name product from database
        for this view.
        """
        if not self.request.GET:
            empty_name = ""
            search_goods = goods_services.get_search_goods(empty_name)
            return search_goods

        search_goods = goods_services.get_search_goods(
            self.request.GET.get("search_form")
        )
        return search_goods

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """
        Returns the dict of item with selected name product from search form
        """

        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.request.GET.get("search_form")
        return context
