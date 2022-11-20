from django.contrib import admin
from django.http import HttpResponseRedirect


from mail.models import EmailTemplate, Subscriber

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass
