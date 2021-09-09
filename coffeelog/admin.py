from django.contrib import admin
from .models import Log, Store, UserLog
# Register your models here.

admin.site.register(Log)
admin.site.register(Store)
admin.site.register(UserLog)