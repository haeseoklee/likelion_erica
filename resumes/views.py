from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume

class ApplyView(LoginRequiredMixin, RedirectView):
    success_url = '/apply/submit/'

def model_form_upload(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            user = get_username(request)
            obj.upload_user = user
            obj.upload_user_real_name = user.profile.real_name
            obj.upload_user_student_number = user.profile.student_number
            obj.upload_user_majoring = user.profile.majoring
            obj.save()
            return render(request, 'resumes/submit.html', {})
        else:
            return render(request, 'resumes/upload.html', {'form':form})
    else:
        form = ResumeForm()
        return render(request, 'resumes/upload.html', {'form': form})

def get_username(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
    return username
