from django.shortcuts import render
from .models import enquiry_table
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def properties(request):
    return render(request, 'properties.html')

def agents(request):
    return render(request, 'agents.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Save to database
        enquiry = enquiry_table(name=name, email=email, phone=phone, message=message)
        enquiry.save()
        
        messages.success(request, 'Your enquiry has been submitted successfully!')
        return render(request, 'contact.html')
        
    return render(request, 'contact.html')

def property_single(request):
    return render(request, 'property-single.html')

def service_details(request):
    return render(request, 'service-details.html')

from django.http import JsonResponse

def data_fetching(request):
    enquiries = enquiry_table.objects.all().order_by('-id')
    return render(request, 'data_fetching.html', {'enquiries': enquiries})

def api_enquiries(request):
    enquiries = enquiry_table.objects.all().order_by('-id').values('name', 'email', 'phone', 'message')
    return JsonResponse(list(enquiries), safe=False)
