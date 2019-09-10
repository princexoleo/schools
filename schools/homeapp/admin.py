from django.contrib import admin
from django import forms
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .models import Registration,Event,EventMemberRegistration
from django.contrib.admin.helpers import ActionForm

class UpdateActionForm(ActionForm):
	user_email = forms.EmailField()

def sending_email(val,e):
        if val:
            #send email
            subject ="Registration confirmation"
            message ="Your registration is complete"
            to_mail = e
            email  = EmailMessage(subject, message, to=e)
            email.send()
            print(e)
            print('Email Send success')
        else:
            print('Sending failed')

def make_published(modeladmin,request, queryset):
      queryset.update(status='True')
      xd = queryset.values('your_email')
      mail = (xd[0].values())
      print(type(mail), mail)
      sending_email(True,e=mail)
make_published.short_description='Send Email to selected person'


# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    
    list_display =(
        'your_name',
        'your_email',
        'status',
    )
    #action_form = UpdateActionForm
    actions =[make_published]
    def get_user_email(self, obj):
        return obj.your_email
    

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Event)

# Register your models here.
class EventMemberRegistrationAdmin(admin.ModelAdmin):
    
    list_display =(
        'your_name',
        'your_email',
        'your_phone_number',
        'transaction_number',
    )
    #action_form = UpdateActionForm
    actions =[make_published]
    def get_user_email(self, obj):
        return obj.your_email
admin.site.register(EventMemberRegistration,EventMemberRegistrationAdmin)
    

