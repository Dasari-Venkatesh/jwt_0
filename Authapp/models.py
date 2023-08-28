from django.db import models

from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPES = [('Client','Client'),
                  ('Admin','Admin'),]
    user_type = models.CharField(choices=USER_TYPES,max_length=10)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="customuser_groups",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="customuser_permissions",
        verbose_name="user permissions"
    )