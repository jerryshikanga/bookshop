from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Account(models.Model):
    """This is a one to one relation to hold the Extra details for a user account"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User Account")
    telephone = models.IntegerField(verbose_name="Telephone Number")
    address = models.TextField(verbose_name="Physical Address")
    picture = models.ImageField(upload_to='accounts/profile/', default="profile_default.png")

    def __str__(self):
        return self.user.get_full_name()

    def get_fields(self):
        return [
            {"name": self.user.get_full_name()},
            {"telephone": self.telephone},
            {"address": self.address},
            {"picture": self.picture},
        ]

    class Meta(object):
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        permissions = (
            ("custom_can_add_user", "Custom Can add User"),
            ("custom_can_edit_user", "Custom Can edit User"),
            ("custom_can_delete_user", "Custom Can delete User"),
        )