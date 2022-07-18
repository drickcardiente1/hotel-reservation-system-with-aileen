from django.contrib import admin
from .models import *

class guest(admin.ModelAdmin):
    list_display = ('id','Email','Name','Arival','Departure','RoomType','Price','Nights','Total','Message')

admin.site.register(Guest, guest)
