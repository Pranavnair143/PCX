from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['mobile','address', 'city','district','state']

admin.site.register(UserProfile,UserProfileAdmin)