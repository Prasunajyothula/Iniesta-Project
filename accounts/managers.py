from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
class CustomAccountManager(BaseUserManager):
    def create_user(
            self, email, username, first_name, last_name, password, **other_fields
    ):
        if not username:
            raise ValueError("You must provide an username")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self, email, username, first_name, last_name, password, **other_fields
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned superuser=True")

        return self.create_user(
            email, username, first_name, last_name, password, **other_fields
        )