from django.contrib import admin
from .models import INCTicket, SRTicket, DeskSideEngr, ServiceDesk, INCChoices, SRChoices, \
    Advisory, Message, SRMessage, Person

admin.site.register(INCTicket)
admin.site.register(SRTicket)
admin.site.register(DeskSideEngr)
admin.site.register(ServiceDesk)
admin.site.register(INCChoices)
admin.site.register(SRChoices)
admin.site.register(Advisory)
admin.site.register(Message)
admin.site.register(SRMessage)
admin.site.register(Person)

# I did editing here
