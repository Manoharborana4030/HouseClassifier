from django.contrib import admin
from .models import *

@admin.register(PredictedImage)
class PredictedImageAdmin(admin.ModelAdmin):
    list_display = ('id','img','category_name','category_id')