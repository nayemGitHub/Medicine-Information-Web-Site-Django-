from django.contrib import admin
from adminApp.models import *

# Register your models here.
class Display_Admin_Panel(admin.ModelAdmin):
    list_display = [
        "display_name",
        "username",
        "admin_email",
        "admin_phone_number"
    ]
admin.site.register(Admin_Panel, Display_Admin_Panel)
admin.site.register(Add_Medicine_Info )
admin.site.register(Add_Blog )



