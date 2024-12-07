from django import forms
from .models import User, Visits
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["firstName", "lastName", "email", "role", "password"]

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class VisitRequestForm(forms.ModelForm):
    class Meta:
        model = Visits
        fields = ["visit_date", "check_out_date", "purpose_of_visit"]
        widgets = {
            "visit_date": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="mm/dd/yyyy"),
            "check_out_date": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="mm/dd/yyyy"),
        }