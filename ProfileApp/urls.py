from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="/"),
    path('getProfile/ById/<str:id>/' , views.profileView , name="profileview"),
    path('create/profile/' , views.addprofile, name="addprofile"),
    path('update/profile/<str:id>/' , views.updateProfile, name="updateProfile"),
    path('delete/profile/<str:id>/' , views.deleteProfile, name="deleteProfile")


]




