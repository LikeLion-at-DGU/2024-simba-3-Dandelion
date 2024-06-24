from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Past)
admin.site.register(Future)
admin.site.register(MyWish)
admin.site.register(SharedWish)