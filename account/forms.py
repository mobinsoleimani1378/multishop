from django import forms
from .models import User, Address
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("phone",)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "password", "is_active", "is_admin"]


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EnterPhoneForm(forms.Form):
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))


class EnterCodeForm(forms.Form):
    code = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('fullname', 'phone', 'email', 'password1', 'password2')


class AddressForm(forms.ModelForm):
    user = forms.IntegerField(required=False)

    class Meta:
        model = Address
        fields = '__all__'
