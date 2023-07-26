from django.urls import path
from main.views import loginfunc, update_userfunc, register, customers, delete_user, update_user

urlpatterns = [
    path('', customers, name='home'),
    path('login/', loginfunc, name='login'),
    path('profile/', update_userfunc, name='update'),
    path('register/', register, name='register'),
    path('user/<int:pk>/', update_user, name='user'),
    path('delete/<int:pk>/', delete_user, name='delete')
]
