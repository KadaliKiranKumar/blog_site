from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponse
import time

def index(request, pk, w):
    return HttpResponse(request.readline())

def blog(request):
    return HttpResponse("Hello, world. This is blodsite")

class ViaDashboardView(TemplateView):
    template_name = 'blog/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(ViaDashboardView, self).get_context_data(**kwargs)

        
        context['visit_time'] = 'Set-Cookie: lastvisit=' + time.asctime(time.localtime())
      
        return context