from django.contrib import admin
from . import models 

admin.site.site_header = "SMS Admin portal"
admin.site.site_title = "SMS Admin portal"

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Application)
admin.site.register(models.Scholarship)
admin.site.register(models.Student)