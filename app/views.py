from django.shortcuts import render

# Create your views here.


def landingPage(request):
    return render(request, 'app/landing/index.html')

# Church
def churchHome(request):
    return render(request, 'app/church/index.html')

def Sermons(request):
    return render(request, 'app/church/sermons.html')

def Events(request):
    return render(request, 'app/church/events.html')

def About(request):
    return render(request, 'app/church/about.html')

def Contact(request):
    return render(request, 'app/church/contact.html')

# Academy
def academyHome(request):
    return render(request, 'app/academy/index.html')

def Classes(request):
    return render(request, 'app/academy/course-grid-4.html')

def Blog(request):
    return render(request, 'app/academy/blog.html')

def Blogs(request):
    return render(request, 'app/academy/blog-single.html')

def Teachers(request):
    return render(request, 'app/academy/teachers.html')

def Perfomance(request):
    return render(request, 'app/academy/pricing.html')

def aboutUs(request):
    return render(request, 'app/academy/about.html')

def contactUs(request):
    return render(request, 'app/academy/contact.html')

