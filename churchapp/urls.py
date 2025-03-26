from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('church_library/', views.church_library, name='church_library'),
    path('men_ministry/', views.men_ministry, name='men_ministry'),
    path('prayer_request/', views.prayer_request, name='prayer_request'),
    path('women_ministry/', views.women_ministry, name='women_ministry'),
    path('youth_ministry/', views.youth_ministry, name='youth_ministry'),
    path('choir_ministry/', views.choir_ministry, name='choir_ministry')
]
#adding static file 
urlpatterns+=staticfiles_urlpatterns()

