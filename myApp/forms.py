from django import forms
from django.core import validators
from myApp.models import Users


class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=False)
    vmail = forms.EmailField(label="verify your email")
    password = forms.CharField(widget=forms.PasswordInput())
    vpassword = forms.CharField(widget=forms.PasswordInput(), label="verify your password")
    #avatar = forms.ImageField()
    bot = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Users
        fields = ('username','email','vmail','password','vpassword', 'bot')

    def clean(self):
        try:
            all_clean_data = super().clean()
            mail1 = all_clean_data.get('email')
            mail2 = all_clean_data.get('vmail')

            pass1 = all_clean_data.get('password')
            pass2 = all_clean_data.get('vpassword')
            if mail1 == mail2 and pass1 == pass2:
                return all_clean_data
            else:
                raise forms.ValidationError("Make sure that mail and passwords are matched")
        except Exception as A:
            print(A)
            raise forms.ValidationError(A)
