from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializer import CustomerSerializer
from . models import Customer,  Purchasing

def main(request):
    return HttpResponse('You entered successfully')


@api_view(['GET'])
def get(request, customer_id):
        purchases = Purchasing.objects.filter(customer_id=customer_id)
        purchase_list = []
        for purchase in purchases:
            purchase_list.append({
                'purchase_id': purchase.purchase_ID,
                'date': purchase.date,
                'items': purchase.items,
            })
        return Response({'purchases': purchase_list})

@api_view(['GET'])
def medicinesget(request, med_ID):
        customer_ids = Purchasing.objects.filter(med_ID=med_ID).values_list('customer_id', flat=True)
        customers = Customer.objects.filter(id__in=customer_ids)
        customer_list = []
        for customer in customers:
            customer_list.append({
                'customer_id': customer.customer_id,
                'name': customer.lname,
                'contact_info': customer.contact_add,
            })
        return Response({'customers': customer_list})

