from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import ProfileModel
from .forms import ProfileRegisterForm, ProfileEditForm, UserEditForm
import register
import accounts

def loginView(request):

    if request.user.is_authenticated and request.user.is_active:
        return HttpResponseRedirect(reverse(register.views.customerListView))


    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):

                return HttpResponseRedirect(request.GET.get('next'))
            
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


        else:
            context = {
                "username": username,
                "errorMessage": "کاربری با این مشخصات یافت نشد ",
            }

            return render(request, 'accounts/login.html', context)

    else:

        return render(request, 'accounts/login.html', {})



def logoutView(request):

    logout(request)


    return HttpResponseRedirect(reverse(accounts.views.loginView))



@login_required
def profileView(request):
    profile = request.user.profile

    context = {
        'profile': profile,
    }

    return render(request, 'accounts/profile.html', context)




def profileRegisterView(request):

    if request.user.is_authenticated and request.user.is_active:
        return HttpResponseRedirect(reverse(register.views.customerListView))

    if request.method == 'POST':
        profileRegisterForm = ProfileRegisterForm(request.POST)

        if profileRegisterForm.is_valid():

            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                                email=profileRegisterForm.cleaned_data['email'],
                                                password=profileRegisterForm.cleaned_data['password'],
                                            first_name=profileRegisterForm.cleaned_data['first_name'],
                                            last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profileModel = ProfileModel(user=user, gender=profileRegisterForm.cleaned_data['gender'])
                                        
            profileModel.save()

            return HttpResponseRedirect(reverse(accounts.views.loginView))
    
    else:

        profileRegisterForm = ProfileRegisterForm()

    context = {
        "formData": profileRegisterForm,
    }

    return render(request, 'accounts/profileRegister.html', context)




def profileEditView(request):

    if request.method == 'POST':
        profileEditForm = ProfileEditForm(request.POST, instance=request.user.profile)
        userEditForm = UserEditForm(request.POST, instance=request.user)

        if profileEditForm.is_valid() and userEditForm.is_valid():
            profileEditForm.save()
            userEditForm.save()

            return HttpResponseRedirect(reverse(accounts.views.profileView))



    else:
        profileEditForm = ProfileEditForm(instance=request.user.profile)
        userEditForm = UserEditForm(instance=request.user)



    context = {
        "profileEditForm": profileEditForm,
        "userEditForm": userEditForm,
    }


    return render(request, 'accounts/profileEdit.html', context)









