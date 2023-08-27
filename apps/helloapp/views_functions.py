from django.shortcuts import render

# Create your views here.

def helloView(request):
    return render(request, "helloView.html")