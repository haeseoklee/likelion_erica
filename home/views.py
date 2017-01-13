from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm


class IndexView(TemplateView):
    template_name = 'home/index.html'

class PhotoView(TemplateView):
    template_name = 'home/photos.html'

class UserRegisterView(FormView):
    template_name = 'registration/user_register.html'
    form_class = UserRegisterForm
    success_url = '/login/'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super(UserRegisterView, self).get(request, *args, **kwargs)
        else:
            return redirect('/')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        real_name = form.cleaned_data.get('real_name')
        phone_number = form.cleaned_data.get('phone_number')
        student_number = form.cleaned_data.get('student_number')
        grade = form.cleaned_data.get('grade')
        register = form.cleaned_data.get('register')
        majoring = form.cleaned_data.get('majoring')

        new_user = User.objects.create(
            username=username,
            email=email,
            )
        new_user.set_password(password)
        new_user.profile.real_name=real_name  # profile is related_name
        new_user.profile.phone_number=phone_number
        new_user.profile.student_number=student_number
        new_user.profile.grade=grade
        new_user.profile.register=register
        new_user.profile.majoring=majoring
        new_user.profile.save()
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)
