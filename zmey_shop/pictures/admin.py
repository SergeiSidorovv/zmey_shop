from django.contrib import admin
from django.utils.safestring import mark_safe, SafeText

from pictures.models import Pictures


class PicturesAdmin(admin.ModelAdmin):
    """
    Displays, allows you to change and add, Pictures data stored in database models on the
    site administrator page
    """

    fields = ["photo", "goods"]
    list_display = ["id", "photo", "goods", "get_html_photo"]
    list_display_links = ["id", "photo"]
    readonly_fields = ["get_html_photo"]

    def get_html_photo(self, picture_object) -> (SafeText | str):
        """Returns a link to the product photo or is it missing"""

        if picture_object.photo:
            return mark_safe(f"<img src='{picture_object.photo.url}' width=50>")
        return "Без фото"


admin.site.register(Pictures, PicturesAdmin)
