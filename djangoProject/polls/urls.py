from django.urls import path
from . import views

urlpatterns = [
    # path(route, view, kwargs, name)
    # route: url pattern
    # view: call view function with a HttpRequest
    # kwargs: Arbitrary keyword arguments can be passed in a dictionary to the target view
    # name: give your url a name
    path('', views.index, name='index'),
]