from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin

from .models import Profile
# Register your models here.
  
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat_allowed')
admin.site.register(Profile,ProfileAdmin)