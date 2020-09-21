from django.urls import path, include
from .views import (
    # home,
    # service,
    contact,
    about,
    HomeView,
    ProductView,ProductListView,
    quality,
    contact_form_submit,
    # product,
    # tea,
    # giftset,whisky,juice,bowl,
    )
from django.conf import settings
from django.conf.urls.static import static


app_name = 'okay_app'


urlpatterns = [

    path('home/', HomeView.as_view(), name='home'),
    path('service/', ProductListView.as_view() ,name='service'),
    path('about/',about,name='about'),
    path('product/<slug>',ProductView.as_view(),name='product'),
    path('contact/',contact,name='contact'),
    path('contact_form_submit/',contact_form_submit,name='contact_form_submit'),
    path('quality/',quality,name='quality'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
