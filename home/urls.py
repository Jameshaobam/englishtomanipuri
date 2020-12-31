
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('home/',views.index, name = "index"),
    path('about',views.about, name = 'about'),
    path('manipuri_word',views.convert, name = 'convert'),
]
