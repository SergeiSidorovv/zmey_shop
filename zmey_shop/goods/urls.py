from django.urls import path

from goods import views


urlpatterns = [
    path("", views.AllGoods.as_view(), name="goods"),
    path("product/<slug:product_slug>/", views.Product.as_view(), name="product"),
    path("search/", views.SearchGoods.as_view(), name="search"),
    path("choice_goods/<str:type_product>/", views.ChoiceGoods.as_view(), name="choice_goods")
]
