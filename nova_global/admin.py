from django.contrib import admin
from django.db import models
from .models import *

admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(Images)
admin.site.register(Partners)