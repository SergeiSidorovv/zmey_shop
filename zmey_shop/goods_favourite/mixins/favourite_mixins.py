from typing import Any
from goods_favourite.services import favourite_services


class GetFavouriteGoodsMixin:
    """Mixin for creating a list of goods added to favorites"""

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """
        Returns the dict of items from Favourite model with user-selected goods,
        from database for this view.
        """

        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context["favourite_goods"] = favourite_services.get_favourite_goods_id(
            user_id=user_id
        )

        return context
