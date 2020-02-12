from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newpeanut', views.new, name='new'),
    path('edit/<int:peanut_id>', views.edit, name='edit')
]
