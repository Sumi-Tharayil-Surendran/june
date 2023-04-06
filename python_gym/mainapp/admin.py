from django.contrib import admin

from mainapp.models import Product
from mainapp.models import EmailWhiteList

# Register your models here.
admin.site.register(Product)
admin.site.register(EmailWhiteList)
