from django.shortcuts import render

# Create your views here.
def past(request):
    return render(request, "post/past.html")