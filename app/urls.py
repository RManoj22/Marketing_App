from django.urls import path
from . import views

urlpatterns = [
    path('',views.details,name='details'),
    path('add/',views.addnew,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]