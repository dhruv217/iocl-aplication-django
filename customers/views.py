from rest_framework import viewsets
from customers.models import Customer
from customers.serializers import CustomerSerializer

class CustomerViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer