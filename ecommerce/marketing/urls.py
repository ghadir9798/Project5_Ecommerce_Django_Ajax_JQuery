from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('ajax/dismiss_marketing_message', views.dismiss_marketing_message, name='dismiss_marketing_message'),
    path('ajax/email_signup', views.email_signup, name='ajax_email_signup'),
] \

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)