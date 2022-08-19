from rest_framework.generics import ListAPIView

from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoriesListAPIView(ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects\
        .filter(food__is_publish=True)\
        .prefetch_related('food', 'food__additional')\
        .order_by('id').all()
