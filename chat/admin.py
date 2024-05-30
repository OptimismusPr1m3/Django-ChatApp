from .models import Chat, Message
from django.contrib import admin

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'created_at', 'author', 'receiver', 'chat') # sind die felder der message, wenn man in die message reingeht -> die die eingetragen sind sieht man auch nur
    list_display = ('text', 'created_at') # das sind die felder die angezeigt werden in der message list , anstatt nur die message nummer zu sehen, sieht man den inhalt und author etc. gleich ohne draufzuklicken
    search_fields = ('author',) # fügt ne suche hinzu die die geschriebenen textfelder in dem tupel durchsucht in dem fall der author

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)