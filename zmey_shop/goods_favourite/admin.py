from django.contrib import admin

from goods_favourite.models import Favourite


class FavouriteAdmin(admin.ModelAdmin):
    """
    Displays, allows you to change and add, Favourite data stored in database models on the
    site administrator page
    """

    list_display = ["id", "user", "goods"]
    fields = ["user", "goods"]
    search_fields = ["id"]


admin.site.register(Favourite, FavouriteAdmin)
