from django.urls import path
from . import views
app_name='item'

urlpatterns=[
    path('<int:pk>/', views.details, name='details'),
    path('new/', views.NewItem, name="NewItem"),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/EditItem/', views.EditItem, name='EditItem'), 
    path("items/", views.items, name='items')
]