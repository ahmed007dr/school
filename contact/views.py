# views.py
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can handle the form data, e.g., send an email
            # form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message']
            return render(request, 'contact/contact.html')  # Redirect or render success page
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})


from .models import Location

def contact_view(request):
    location = Location.objects.first()  # Adjust as needed (e.g., get by id)
    return render(request, 'contact/contact.html', {'location': location})
