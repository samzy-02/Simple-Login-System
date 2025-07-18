from django.shortcuts import render, redirect
from . forms import ContactForm
# Create your views here.
def Home(request):
    return render(request, "Home.html")


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.message()
            return redirect('success-page')
    else:
        form = ContactForm()
    return render(request, 'contact_page.html', {'form':form})



def success_page(request):
    return render(request, 'success_page.html')