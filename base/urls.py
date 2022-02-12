from django.urls import path
from .views import owner_view, pet_view, ownerCreat, petCreat,petUpdate,ownerUpdate, customLoginView, RegisterPage,pet_Detail,owner_Detail,petDelete
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',customLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),
    path('',pet_view.as_view(), name='pets'),
    path('owners',owner_view.as_view(), name='owners'),
    path('owner-create',ownerCreat.as_view(), name='owner-create'),
    path('pet-create',petCreat.as_view(), name='pet-create'),
    path('pet-update/<pk>/',petUpdate.as_view(), name='pet-update'),
    path('owner-update/<pk>/',ownerUpdate.as_view(), name='owner-update'),
    path('pet-delete/<pk>/',petDelete.as_view(), name='pet-delete'),

    path('p/<int:pk>/',pet_Detail.as_view(), name='pet-view'),
    path('o/<int:pk>/',owner_Detail.as_view(), name='owner-view'),

]