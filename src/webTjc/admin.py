from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Merch)
admin.site.register(AboutImages)
admin.site.register(Register)
admin.site.register(Contact)


