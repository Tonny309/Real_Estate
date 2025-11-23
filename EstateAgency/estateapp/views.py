from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')

def agents(request):
    return render(request, 'agents.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def properties(request):
    return render(request, 'properties.html')

def propertysingle(request, id):
    # You can fetch property from DB later using id
    return render(request, 'property-single.html', {'id': id})

def servicedetails(request):
    return render(request, 'service-details.html')


def services(request):
    return render(request, 'services.html')

def starterpage(request):
    return render(request, 'starter-page.html')
