from django.contrib import admin

from .models import Athlete, Event
# Register your models here.


admin.site.register(Event)
admin.site.register(Athlete)