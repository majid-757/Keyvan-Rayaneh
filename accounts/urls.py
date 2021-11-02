from django.urls import path

from .views import loginView, logoutView, profileView, profileRegisterView, profileEditView


urlpatterns = [
    path('login/', loginView),
    path('logout/', logoutView),
    path('profile/', profileView),
    path('profileRegister/', profileRegisterView),
    path('profileEdit/', profileEditView),
]







