from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('accounts/logout', views.logout_view, name='auth_logout'),
    path('accounts/login/', views.login_view, name='auth_login'),
    path('accounts/register', views.registration_view, name='auth_register'),
    path('accounts/address/add/', views.add_user_address, name='add_user_address'),
    path('accounts/activate/<str:activation_key>', views.activation_view, name='activation_view'),
    path('ajax/add_user_address', views.add_user_address, name='ajax_add_user_address'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)