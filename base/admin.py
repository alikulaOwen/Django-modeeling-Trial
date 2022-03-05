from django.contrib import admin

from .models import Document, ProteinSequence, Comment, Notification,NotificationType,Link

# Register your models here.
admin.site.register(Document)
admin.site.register(ProteinSequence)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(NotificationType)
admin.site.register(Link)
