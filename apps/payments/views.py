from rest_framework import viewsets, mixins
from apps.accounts.permissions import IsSuperUser, IsReceptionist
from apps.payments.serializers import PaymentSerializer
from apps.payments.models import Payment

class PaymentAdminViewSet (
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsSuperUser | IsReceptionist]
