from django import template

from goods.services import goods_services


register = template.Library()

@register.inclusion_tag("goods/type_goods.html")
def get_types_goods():
    types_goods = goods_services.get_all_category_name()
    return {"types_goods": types_goods}
