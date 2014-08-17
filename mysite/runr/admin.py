from django.contrib import admin

from runr.models import Timer

class TimerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields':['key', 'end_time']}),
        ('Optional', {'fields':['text', 'creator']}),
    ]
    
    list_display = ('key', 'end_time', 'expired')

admin.site.register(Timer, TimerAdmin)
