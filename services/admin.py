from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="Admin Panel"
admin.site.site_title="Admin Panel"
admin.site.site_index_title="Admin Panel"
admin.site.register(Land)
admin.site.register(Products)
admin.site.register(Laundry)
