from django.contrib import admin
from accounts.models import items,spent,category
# Register your models here.

admin.site.register(items)
admin.site.register(spent)
admin.site.register(category)