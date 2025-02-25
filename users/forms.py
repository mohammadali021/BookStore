from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'نام خود را وارد نمایید',
                                      'style': 'width:200;height:40px;text-transform:None;'}),
    )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'نام خانوادگی خود را وارد نمایید',
                                      'style': 'width:200;height:40px;text-transform:None;'}),
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'ایمیل خود را وارد نمایید',
                                       'style': 'width:200;height:40px;text-transform:None;'}),
    )
    username = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'نام کاربری خود را وارد نمایید',
                                      'style': 'width:200;height:40px;text-transform:None;'}),
    )
    password1 = forms.CharField(
        label="",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={'class': "form-control", 'placeholder': 'کلمه عبور خود را وارد نمایید', 'name': 'password1',
                   'type': 'password', 'style': 'width:200;height:40px;text-transform:None;'}),
    )
    password2 = forms.CharField(
        label="",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={'class': "form-control", 'placeholder': 'تکرار کلمه عبور', 'name': 'password2',
                   'type': 'password', 'style': 'width:200;height:40px;text-transform:None;'}), )

    class Meta:
        model = User
        fields = ('name', 'last_name', 'email', 'username', 'password1', 'password2')


class EditInfo(forms.Form):
    # first_name = forms.CharField(
    #     label="",
    #     max_length=50,
    #     required=False,
    #     widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'نام خود را وارد نمایید',
    #                                   'style': 'width:200;height:40px;text-transform:None;'}),
    # )
    # last_name = forms.CharField(
    #     label="",
    #     max_length=50,
    #     required=False,
    #     widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'نام خانوادگی خود را وارد نمایید',
    #                                   'style': 'width:200;height:40px;text-transform:None;'}),
    # )
    #
    #
    # email = forms.CharField(
    #     label="",
    #     max_length=50,
    #     required=False,
    #     widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'ایمیل خود را وارد نمایید',
    #                                   'style': 'width:200;height:40px;text-transform:None;'}),
    # )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

