from django import forms
from django.forms import Form
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '아이디'})
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호'})
        )
    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("존재하지 않은 아이디 입니다.")
        return username

class UserRegisterForm(Form):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '아이디'})
        )
    real_name = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': '이름'})
        )
    phone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': '전화번호  ex) 01012345678'})
        )
    student_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': '학번'})
        )
    majoring = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': '학과'})
        )
    grade = forms.CharField(
        widget=forms.Select(choices=UserProfile.GRADE_CHOICES),
        max_length=2,
        )
    register = forms.CharField(
        widget=forms.Select(choices=UserProfile.REGISTER_CHOICES),
        max_length=2,
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': '이메일'})
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호'})
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 확인'})
        )

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError('중복된 아이디 입니다.')
        if len(username)>15:
            raise forms.ValidationError('아이디의 길이가 너무 깁니다.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError('중복된 이메일 입니다.')
        return email
