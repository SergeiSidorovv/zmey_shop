from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import View
from django.shortcuts import redirect

from goods_favourite.models import Favourite
from goods_favourite.services import favourite_services


class FavouriteGoods(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Favourite
    template_name = "goods_favourite/favourite_goods_view.html"
    context_object_name = "favourites"

    def get_queryset(self):
        return favourite_services.get_favourite_goods(self.request.user.id)


class ManageFavouriteGoods(View):
    def post(self, request, id_product):
        product = favourite_services.get_favourite_product(request.user.id, id_product)
        if not product:
            favourite_services.create_product_in_favourite(request.user.id, id_product)
            return redirect(request.META.get("HTTP_REFERER"))
        favourite_services.delete_favourite_product(product)
        return redirect(request.META.get("HTTP_REFERER"))
