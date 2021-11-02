from django.urls import path

from .views import customersRegisterView, customerListView, customerDetailsView, customerEditView


urlpatterns = [
    path('', customersRegisterView),
    path('customerList/', customerListView),
    path('customerDetails/<int:customer_id>', customerDetailsView),
    path('customerEdit/<int:customer_id>', customerEditView),

]







