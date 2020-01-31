from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    # null=True 는 필드의 값이 NULL로 데이터베이스에 저장되는 것을 허용
    # blank=True 는 필드가 폼에서 빈 채로 저장되는 것을 허용
    username = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(unique=True)

    # A string describing the name of the field on the user model that is used as the unique identifier.
    # The field must be unique (unique=True)
    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS must contain all required fields on your user model,
    # but should not contain the USERNAME_FIELD or password as these fields will always be prompted for.
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name'
    ]

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
