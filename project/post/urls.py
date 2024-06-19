from django.urls import path
from .views import *

app_name = "post"
urlpatterns = [
    path('past/', past, name="past"),
    path('past_result/', past_result, name="past_result"),
    path('start_108/', start_108, name="start_108"),
    path('init_108/', init_108, name="init_108"),
    path('do_108/', do_108, name="do_108"),
    path('post_108/', post_108, name="post_108"),
    path('community_108/', community_108, name="community_108"),
]