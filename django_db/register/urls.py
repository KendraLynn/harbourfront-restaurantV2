from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.reg_view, name='register'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    path('update_view/<int:id>', views.update_view, name='update_view'),
    path('update_view/update/<int:id>', views.update, name='update'),
]
