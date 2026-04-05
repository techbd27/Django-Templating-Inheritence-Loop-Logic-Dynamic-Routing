from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def demo(request):
    # return HttpResponse("Hello, welcome to the home page!")
    person = {
        'name': 'John Doe',
        'age': 30,
        'hobbies': ['Reading', 'Traveling', 'Cooking'], # array of hobbies
        'city': 'New York'
    }    # This is a tuple containing the person's information
    
    return render(request, 'index.html', {
        'person': person,
    })
 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def greet(request, person):
    display = request.GET.get('display','Default Value')
    page_number = request.GET.get('p',1)
    return render(request, 'person.html', {'person':person,'display':display, 'page_number':page_number})

def favnum(request, n):
    return HttpResponse('Your favorite number is: ' + str(n))
     