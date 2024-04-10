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
        category_name = self.kwargs["type_product"]
        choice_goods = goods_services.get_all_goods_for_category(
            category=category_name
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
        slug_product = self.kwargs["product_slug"]

        context["product"] = goods_services.get_product(slug=slug_product)
        if not context["product"]:
            logger.info("Такокго товара нет, страница не найдена")
            raise Http404()

        product_id = context["product"].get().id
        context["pictures"] = picture_services.get_pictures_from_goods_id(
            product_id=product_id
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
        check_search_name = self.request.GET
        if not check_search_name:
            empty_name = ""
            search_goods = goods_services.get_search_goods(empty_name)
            return search_goods

        search_name = self.request.GET.get("search_form")
        search_goods = goods_services.get_search_goods(
            name_product=search_name
        )
        return search_goods
