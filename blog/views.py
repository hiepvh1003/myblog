from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post, About

def PostListView(request):
    Data = {'Posts': Post.objects.all().order_by("created_date")}
    return render(request, 'pages/home.html', Data)

def AboutListView(request):
    AboutData = {'Abouts': About.objects.all().order_by("id")}
    return render(request, 'pages/about.html', AboutData)

class ResumeView(TemplateView):
    template_name = "pages/resume.html"
