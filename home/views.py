from django.shortcuts import render

#Function to display home page

def home(request):
    """
    A view to show the home page
    """
    return render(request, "home/index.html")
