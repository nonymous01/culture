from django.contrib import admin
from auth_app.models import Utilisateur,ServiceRequest
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','password')


admin.site.register(Utilisateur, UserAdmin)
admin.site.register(ServiceRequest)

