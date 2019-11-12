from showapi.views import Movie_Views,Seat_views,Show_Views
from django.urls import path,include
from rest_framework.routers import SimpleRouter

app_Router = SimpleRouter()
app_Router.register('movie',Movie_Views)
app_Router.register('shows',Show_Views)
app_Router.register('seats',Seat_views)

urlpatterns = [
    path('',include(app_Router.urls))
]
