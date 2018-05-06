from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^portfolio/', views.portfolio, name='portfolio'),

]