from django.db import models


# Create your models here.
class SystemUser(models.Model):
    user_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=10, unique=True, default=None, null=True)

    class Meta:
        db_table = "system_user"
        # verbose_name = _('system_user')
        # verbose_name_plural = _('System Users')


class Client(models.Model):
    user = models.ForeignKey(to=SystemUser, on_delete=models.CASCADE, related_name='user_client')
    name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'client'


class UserFiles(models.Model):
    image = models.FileField(upload_to='apifiles', default=None, null=True, blank=True)

    class Meta:
        db_table = 'user_files'
