from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import CustomerRegistration
from .forms import SearchForm, CustomerForm

import register
import accounts


@login_required
def customersRegisterView(request):
    # if request.user.is_authenticated and request.user.is_active:

        if request.method == 'POST':

            customerForm = CustomerForm(request.POST)

            if customerForm.is_valid():
                customerForm.save()

                return HttpResponseRedirect(reverse(register.views.customersRegisterView))
        else:
            customerForm = CustomerForm()

        context = {
            'customerForm': customerForm
            
        }

        return render(request, 'register/index.html', context)

    # else:

    #     return HttpResponseRedirect(reverse(accounts.views.loginView))



@login_required
def customerListView(request):

    # if request.user.is_authenticated and request.user.is_active:

        searchForm = SearchForm(request.GET)

        if searchForm.is_valid():

            SearchText = searchForm.cleaned_data["SearchText"]

            customers = CustomerRegistration.objects.filter(firstname__contains=SearchText)

        else:

            customers = CustomerRegistration.objects.all()

        context = {
            'customerList': customers,
            'searchForm': searchForm,
        }


        return render(request, 'register/customerList.html', context)
    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.loginView))



@login_required
def customerDetailsView(request, customer_id):

    # if request.user.is_authenticated and request.user.is_active:

        customer = CustomerRegistration.objects.get(pk=customer_id)




        context = {
            'customerDetails': customer,
        }


        return render(request, 'register/customerDetails.html', context)

    # else:

    #     return HttpResponseRedirect(reverse(accounts.views.loginView))




def customerEditView(request, customer_id):

    customer = CustomerRegistration.objects.get(pk=customer_id)

    if request.method == 'POST':

        customerForm = CustomerForm(request.POST, instance=customer)

        if customerForm.is_valid():

            customerForm.save()

            return HttpResponseRedirect(reverse(register.views.customerListView))
    else:

        customerForm = CustomerForm(instance=customer)

    context = {
        "customerForm":customerForm
    }

    return render(request, 'register/customerEdit.html', context)




