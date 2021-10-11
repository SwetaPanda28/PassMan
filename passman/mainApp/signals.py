from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from . import models

@receiver(user_logged_in,sender=models.User)
def createManager(sender,user,*args,**kwargs):
    manager,created=models.PasswordManager.objects.get_or_create(user=user)
    if(created):
        manager.save()