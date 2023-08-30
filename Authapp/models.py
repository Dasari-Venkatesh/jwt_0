from django.db import models

from django.contrib.auth.models import AbstractUser,Group,Permission,BaseUserManager

# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self,username, email,user_type, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, **extra_fields)
#         user.user_type=user_type
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self,username, email, user_type,password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, user_type, username,password, **extra_fields)



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
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['user_type','email']

    def __str__(self):
        return self.username