from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/templates/index.html')  # Points to templates/myapp/index.html
