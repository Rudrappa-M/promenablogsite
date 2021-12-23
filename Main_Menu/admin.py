from django.contrib import admin

# Register your models here.

from Main_Menu.models import category, mainmenu

admin.site.register(category)
admin.site.register(mainmenu)
