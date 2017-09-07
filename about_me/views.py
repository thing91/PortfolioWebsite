from django.shortcuts import render

def index(request):
    return render(request, 'about_me/home.html')

def contact(request):
    return render(request, 'about_me/contact.html')

##def exp(request):
##    return render(request, 'about_me/exp.html')

def expv2(request):
    return render(request, 'about_me/expv2.html')

def skills(request):
    return render(request, 'about_me/skills.html')

def interests(request):
    return render(request, 'about_me/interests.html')
