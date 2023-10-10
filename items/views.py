from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from items.models import Category, Item
from items.serializers import CategorySerializer, ItemSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_items(request):
    items = Item.objects.filter(category_id=request.data['category'])
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)