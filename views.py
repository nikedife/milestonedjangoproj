from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def element(request):
    return render(request,'elements.html')

def testimonial(request):
    return render(request,'services.html')

def video(request):
    return render(request,'video.html')
