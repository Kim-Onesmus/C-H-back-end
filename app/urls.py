from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    
    path('churchHome', views.churchHome, name='churchHome'),
    path('sermons', views.Sermons, name='sermons'),
    path('events', views.Events, name='events'),
    path('about', views.About, name='about'),
    path('contact', views.Contact, name='contact'),
    
    path('academyHome', views.academyHome, name='academyHome'),
    path('classes', views.Classes, name='classes'),
    path('blog', views.Blog, name='blog'),
    path('blogs', views.Blogs, name='blogs'),
    path('teachers', views.Teachers, name='teachers'),
    path('perfomance', views.Perfomance, name='perfomance'),
    path('about_us', views.aboutUs, name='about_us'),
    path('contact_us', views.contactUs, name='contact_us'),
]