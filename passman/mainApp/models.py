from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from cryptography.fernet import Fernet
import base64
import hashlib
# Create your models here.



class PasswordManager(models.Model):
    key=models.CharField(max_length=1000)
    salt=models.CharField(max_length=1000,null=True,blank=True)
    user=OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}({self.user.id})'s passwords"

    def save(self,*args,**kwargs):
        if(self._state.adding):
            self.salt=Fernet.generate_key().decode()
        super(PasswordManager,self).save(*args,**kwargs)



class Password(models.Model):
    website=models.URLField(blank=False,null= False)
    username=models.CharField(null=True,max_length=100)
    password=models.CharField(null=True,max_length=100)
    manager=models.ForeignKey(PasswordManager,on_delete=models.CASCADE)
    changingPass=models.BooleanField(null=True,default=False)




    # def save(self,key='shax',changedPass=False,*args,**kwargs):

    #     if(self.changingPass):
    #         self.changingPass=False
    #         changedPass=True

    #     if(not self._state.adding and  hashlib.sha512(key.encode()).hexdigest()!=self.manager.key):
    #         raise Exception('wrong key')

    #     if(self._state.adding or changedPass):
    #         salt=self.manager.salt.encode()
    #         actualkey=get_actual_key(key,salt)
    #         print(actualkey)
    #         fernet=Fernet(actualkey)
    #         new_var = fernet.encrypt(self.password.encode()).decode()
    #         self.password=new_var
            
    #     super(Password,self).save(*args,**kwargs)

    def __str__(self) :
        return f'{self.manager} for {self.website} as {self.username}'



# def get_actual_key(key,salt):
#     salt=base64.urlsafe_b64decode(salt)
#     key=key.encode()
#     return base64.urlsafe_b64encode((salt+key)[len(key):])
    