from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('id')

    # Adiciona autenticação via Token
    authentication_classes = [TokenAuthentication]

    # Permite acesso apenas a usuários autenticados
    permission_classes = [IsAuthenticated]