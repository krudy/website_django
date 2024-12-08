from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .form import UploadImageForm

from django.views import View 
from django.shortcuts import render, redirect
from .models import Image

def custom_logout(request):
    logout(request)
    return redirect('giffy_app:index')

class IndexView(View):
    def get(self, request):
        images = Image.objects.order_by('upload_date')
        return render(request, 'giffy_app/index.html', {'images': images})
    
class SignupView(View):
    def get(self, request):
        return render(request,
                      'giffy_app/signup.html',
                      {
                          'form': UserCreationForm()
                      })
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data['username']
            password = form.data['password1']
            user = authenticate(
                request,
                username=username,
                password=password,
                )
            if user:
                login(request, user)
                return redirect('/')
        else:
            return render(request,
                          'giffy_app/signup.html',
                          {
                              'form': form,
                          })

class UploadImageView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        return render(request,
                      'giffy_app/upload.html',
                      {
                          'form': UploadImageForm()
                      })
        
    def post(self, request):
        user = request.user
        
        if not user.is_authenticated:
            raise Exception('You must be logged in')
        form = UploadImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            image = Image(
                title = form.data['title'],
                image = form.files["image"],
                upload_date = datetime.now(),
                uplouded_by = user,
            )
            image.save()
            return redirect('/')
        return render(request,
                      'giffy_app/upload.html',
                      {
                          'form': form,
                          'error': 'Invalid form data'
                      })