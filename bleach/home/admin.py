from django.contrib import admin
from .models import animeinfo,mangaka,CensorInfo,studio
# Register your models here.
admin.site.register(animeinfo)
admin.site.register(mangaka)
admin.site.register(CensorInfo)
admin.site.register(studio)
"""adds already created models to the 
django administration for admin operations"""