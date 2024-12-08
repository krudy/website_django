from django.views import View 
from django.shortcuts import render
from .models import Image

class IndexView(View):
    def get(self, request):
        images = Image.objects.order_by('upload_date')
        return render(request, 'giffy_app/index.html', {'images': images})
    
