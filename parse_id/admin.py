from django.contrib import admin

# Register your models here.
from .models import id_desc
from .models import upload

admin.site.register(id_desc)
admin.site.register(upload)
