from django.contrib import admin
from django.utils.safestring import mark_safe, SafeText

from goods.models import Goods, CategoryGoods



class GoodsAdmin(admin.ModelAdmin):
    """
    Displays, allows you to change and add, Goods data stored in database models on the site
    administrator page
    """

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
        "category",
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
        "category",
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
        "category",
    ]
    list_select_related = ["category"]
    search_fields = ["name", "slug", "article"]
    readonly_fields = ["get_html_main_photo"]
    prepopulated_fields = {"slug": ("name",)}

    def get_html_main_photo(self, picture_object) -> (SafeText | str):
        """Returns a link to the main product photo"""

        if picture_object.main_photo:
            return mark_safe(f"<img src='{picture_object.main_photo.url}' width=50>")
        return "Без фото"


class CategoryGoodsAdmin(admin.ModelAdmin):
    """
    Displays CategoryGoods data stored in database models on the site administrator page
    """

    list_display = ["id", "name", "slug"]
    list_display_links = ["name", "slug"]
    fields = ["name", "slug"]
    search_fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Goods, GoodsAdmin)
admin.site.register(CategoryGoods, CategoryGoodsAdmin)
