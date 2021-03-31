from django.contrib import admin
from .models import Container, Command, Transfer

# Register your models here.
admin.site.register(Container)
admin.site.register(Command)
admin.site.register(Transfer)
