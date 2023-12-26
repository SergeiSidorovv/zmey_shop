from django.contrib import admin
from django.utils.safestring import mark_safe

from goods.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slug",
        "color",
        "photo",
        "get_html_photo",
    ]
    readonly_fields = ["get_html_photo"]
    list_display_links = ["id", "name"]
    fields = ["name", "slug", "color", "photo", "get_html_photo"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        return "Без фото"


admin.site.register(Goods, GoodsAdmin)
