from django.urls import path
from .views import *

app_name = "post"
urlpatterns = [
    path('past/', past, name="past"),
    path('past_result/', past_result, name="past_result"),
    path('future/', future, name="future"),
    path('future_result/', future_result, name="future_result"),
]
