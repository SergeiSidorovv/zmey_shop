from typing import Any
from goods.models import Goods

from goods_favourite.services import favourite_services


class BaseDataMixin:
    model = Goods
    paginate_by = 15

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["favourite_goods"] = favourite_services.get_favourite_goods_id(
            self.request.user.id
        )
        return context
