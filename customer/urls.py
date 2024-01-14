from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('purchase/', views.get),
    path('medicines/', views.medicinesget),
]