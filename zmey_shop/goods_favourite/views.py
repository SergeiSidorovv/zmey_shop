from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser

from goods_favourite.models import Favourite
from goods_favourite.services import favourite_services
from goods.mixins.goods_mixins import BaseDataMixin


class FavouriteGoods(LoginRequiredMixin, BaseDataMixin, ListView):
    """Transfers all goods added to the Favourite from the database to the template page"""

    model = Favourite
    template_name = "goods_favourite/favourite_goods_view.html"
    context_object_name = "favourites"

    def get_queryset(self):
        """Returns the list of items Favourite model from database for this view."""

        user_id = self.request.user.id
        favourite_goods = favourite_services.get_favourite_goods(user_id=user_id)
        return favourite_goods


class ManageFavouriteGoods(View):
    """Checks the product for its presence in favorites and passes it to the template"""

    def post(self, request, id_product: int):
        """
        Adds an item to favorites or delete it, and then returns the user to the same page
        """

        if request.user == AnonymousUser():
            previous_page = request.META.get("HTTP_REFERER")
            return redirect(previous_page)

        user_id = request.user.id
        product = favourite_services.get_favourite_product(user_id=user_id, id_product=id_product)
        if not product:
            favourite_services.create_product_in_favourite(user_id=user_id,id_product=id_product)
            return redirect(previous_page)
        favourite_services.delete_favourite_product(product)
        return redirect(previous_page)
