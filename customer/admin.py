from django.contrib import admin
from .models import Customer, Pharmacy, Medicines, Purchasing, Sales, Reports

admin.site.register(Customer)
admin.site.register(Pharmacy)
admin.site.register(Medicines)
admin.site.register(Purchasing)
admin.site.register(Sales)
admin.site.register(Reports)