from django.contrib import admin

# Register your models here.
from .models import Personal, Polling, Family

admin.site.register(Personal)
admin.site.register(Polling)
admin.site.register(Family)
