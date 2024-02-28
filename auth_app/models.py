
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = _("ADMIN"), _("Admin")

    base_type = Role.ADMIN

    account_type = models.CharField(
        _("Account Type"), max_length=50, choices=Role.choices
    )
    def save(self, *args, **kwargs):
        if not self.pk and not self.account_type:
            self.account_type = self.base_type
        super().save(*args, **kwargs)

    def __str__(self):
        if self.get_username:
            return f"{self.get_username()}"
        return f"{self.first_name} {self.last_name}"

