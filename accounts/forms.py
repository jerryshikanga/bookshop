from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from .models import Account

User = get_user_model()


class UserCreateForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=999)
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput,
                                label="Enter desired password")
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput,
                                label="Repeat the password entered")
    address = forms.CharField(max_length=1000, required=True, widget=forms.Textarea)

    # group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False) # removed group in favor of permissions which can be customised based in individual user
    permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), label="Choose user permissions", required=False)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords must match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address is already in use")
        return email

    def save_user(self):
        form_data = self.data
        user = User.objects.create(
            first_name=form_data.get("first_name"),
            last_name=form_data.get("last_name"),
            email=form_data.get("email"),
            username=form_data.get("email"),
        )
        user.set_password(form_data.get("password1"))

        # did away with groups in favor of permissions
        # group = form_data.get("group")
        # if group and group is not None :
        #     user.groups.add(group)
        permissions = form_data.get("permissions", None)
        [user.user_permissions.add(permission) for permission in permissions]
        user.save()

        account = Account.objects.create(
            user=user,
            telephone=form_data.get("telephone"),
            address=form_data.get("address")
        ).save()

        return account
