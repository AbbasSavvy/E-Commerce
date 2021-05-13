from django.contrib import admin

# Register your models here.
from user.models import User1Profile
from user.models import User2Profile

class User1ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address','city','state','pin_code','country']
    list_filter = ['city','state','pin_code','country']

class User2ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone']

admin.site.register(User1Profile,User1ProfileAdmin)
admin.site.register(User2Profile,User2ProfileAdmin)