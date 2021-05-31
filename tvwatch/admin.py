from django.contrib import admin

from .models import Tvshow, Mylist, Newsletter
admin.site.register(Tvshow)
admin.site.register(Mylist)
admin.site.register(Newsletter)
# Register your models here.
