from django.urls import path
from .views import *

app_name = "post"
urlpatterns = [
    path('past/', past, name="past"),
]
