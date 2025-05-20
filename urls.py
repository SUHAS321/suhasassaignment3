from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),                   # Main page with list of days
    path('monday', views.monday, name='monday.html'),
    path('tuesday', views.tuesday, name='tuesday.html'),
    path('wednesday', views.wednesday, name='wednesday.html'),
    path('thursday', views.thursday, name='thursday.html'),
    path('friday', views.friday, name='friday.html'),
    path('saturday', views.saturday, name='saturday.html'),
    path('sunday', views.sunday, name='sunday.html')
]
