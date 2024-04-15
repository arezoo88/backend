from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        email_username, mobile = self.email.split("@")
        if self.full_name in ['', None]:
            self.full_name = email_username
        if self.username in ['', None]:
            self.username = email_username
        super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to='image', default='default/default-user.jpg', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pid = ShortUUIDField(unique=True, length=10,
                         max_length=20, alphabet='abcdefghijk')

    def __str__(self):
        return self.user.full_name
