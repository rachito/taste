from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Perfil del usuario"""
    user = models.OneToOneField(User)
    sex = models.CharField(max_length=1, null=True, blank=True)
    accepted_eula = models.BooleanField()

    def __unicode__(self):
        return ''.join(["Profile Of ", self.user.first_name])
