from django import forms
from django.core import validators
from myApp.models import Users, Contacts


class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    vmail = forms.EmailField(label="verify your email")
    phoneNumber = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    vpassword = forms.CharField(widget=forms.PasswordInput(), label="verify your password")
    about = forms.CharField(widget=forms.Textarea)
    avatar = forms.ImageField()
    bot = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Users
        fields = ('username','first_name','last_name','email','vmail','phoneNumber','password','vpassword', 'about','avatar', 'bot')

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

