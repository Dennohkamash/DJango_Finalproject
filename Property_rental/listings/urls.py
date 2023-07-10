from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name="listings"),
    path('login/', views.loginPage, name="login"),
    path('signup/', views.registerPage, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('property/', views.property, name="property"),
    path('blogs/', views.blogs, name="blogs"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('listing/<pk>/', views.listing, name="listing"),
    path('create/', views.create_listing, name="create_listing" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)