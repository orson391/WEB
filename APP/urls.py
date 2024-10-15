from django.contrib import admin
from django.urls import path
from APP import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='Home'),
    path('about',views.about,name='About'),
    path('services',views.services,name='Services'),
    path('contact',views.contact,name='Contact'),
    #path('',views.contact,name='Contact'),
]
