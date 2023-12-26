from django.contrib import admin

from goods_favourite.models import Favourite


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "goods"]
    fields = ["user", "goods"]
    search_fields = ["id"]


admin.site.register(Favourite, FavouriteAdmin)
