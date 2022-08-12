from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Profile(models.Model):
   user     = models.OneToOneField(User, verbose_name= _("User"), on_delete=models.CASCADE)
   birthday = models.DateField(_("Date of Birth"), blank=True, null=True)
   photo    = models.ImageField(_("Profile Image"), upload_to='user_img/%Y/%m/%d/', blank=True)

   def __str__(self):
       return self.user.username
   