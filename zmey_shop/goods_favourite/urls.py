from django.urls import path

from goods_favourite import views

app_name = "favourite"

urlpatterns = [
    path("", views.FavouriteGoods.as_view(), name="favourite_goods"),
    path("<int:id_product>", views.ManageFavouriteGoods.as_view(), name="add"),
]
