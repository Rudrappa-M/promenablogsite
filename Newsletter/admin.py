from django.contrib import admin

# Register your models here.


# Register your models here.

from Newsletter.models import Newsletter,Subscription


admin.site.register(Subscription)
admin.site.register(Newsletter)

