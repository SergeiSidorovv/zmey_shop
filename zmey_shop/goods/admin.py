from django.contrib import admin
from django.utils.safestring import mark_safe, SafeText

from goods.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slug",
        "article",
        "description",
        "yarn",
        "composition",
        "additional_materials",
        "color",
        "main_photo",
        "get_html_main_photo",
    ]
    list_display_links = [
        "id",
        "name",
        "slug",
        "article",
        "description",
        "yarn",
        "composition",
        "additional_materials",
        "color",
        "main_photo",
    ]
    fields = [
        "name",
        "slug",
        "article",
        "description",
        "yarn",
        "composition",
        "additional_materials",
        "color",
        "main_photo",
    ]
    search_fields = ["name", "slug", "article"]
    readonly_fields = ["get_html_main_photo"]
    prepopulated_fields = {"slug": ("name",)}

    def get_html_main_photo(self, picture_object) -> (SafeText | str):
        if picture_object.main_photo:
            return mark_safe(f"<img src='{picture_object.main_photo.url}' width=50>")
        return "Без фото"


admin.site.register(Goods, GoodsAdmin)
