from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


from mainapp.models import Product

from .managers import CustomUserManager
from django.core.mail import send_mail


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product)
    date_joined = models.DateTimeField(default=timezone.now)
    signup_confirmation = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_object(self):
        obj = CustomUser.objects.get(user=self.request.user)
        return obj

    def email_user(self, *args, **kwargs):
        result = send_mail(
            '{}'.format(args[0]),
            '{}'.format(args[1]),
            'fajarpm@hotmail.com',
            [self.email],
            fail_silently=False,
        )
        print(result)


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
    instance.save()
