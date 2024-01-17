from django.contrib import admin
from django.utils.safestring import mark_safe, SafeText

from goods.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "main_photo","slug", "color", "get_html_main_photo"]
    list_display_links = ["id", "name", "main_photo"]
    fields = ["name", "slug", "color", "main_photo"]
    search_fields = ["name"]
    readonly_fields = ["get_html_main_photo"]
    prepopulated_fields = {"slug": ("name",)}

    def get_html_main_photo(self, picture_object) -> (SafeText | str):
        if picture_object.main_photo:
            return mark_safe(f"<img src='{picture_object.main_photo.url}' width=50>")
        return "Без фото"


admin.site.register(Goods, GoodsAdmin)
