from django.contrib import admin

# Register your models here.
from .models import Clipboard
from django.contrib.sessions.models import Session

admin.site.register(Session)

admin.site.register(Clipboard)
class Clipboard(admin.ModelAdmin):
    list_display =  '__all__'

