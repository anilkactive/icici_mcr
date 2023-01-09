from django.contrib import admin
from .models import Room, Incharge, Token, Display_call

# Register your models here.
class InchargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'incharge_name')
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_name')
class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'tok_no', 'room', 'call_time', 'served_time')
class Display_callAdmin(admin.ModelAdmin):
    list_display = ('id', 'd_room_no')

admin.site.register(Room, RoomAdmin)
admin.site.register(Incharge, InchargeAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Display_call, Display_callAdmin)
