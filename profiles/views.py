from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm
from django.conf import settings

from django.core.mail import send_mail



# Create your views here.
def Home(request):
    return render(request,'home.html')


# def Profile_create(request):
#     profiles=Profile.objects.all()
#
#     if request.method == 'POST':
#         form=ProfileForm(request.POST,files=request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             form=ProfileForm()
#
#     return render(request,'home.html', {'form':form})

def home(request):
    return render(request,'home.html')

def Profile_create(request):

    profiles=Profile.objects.all()

    if request.method=='POST':

        form=ProfileForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()

            return redirect('profilelist')

    else:
        form =ProfileForm()

    return render(request,'profiles.html',{'form':form,'books':profiles})

def ProfileList(request):

    profiles=Profile.objects.all()

    paginator=Paginator(profiles,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)


    return render(request,'prifilelist.html',{' profiles': profiles,'page':page})

def Portfolio(request):

    return render(request,'portfolio.html')

def about(request):

    return render(request,'about.html')


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#
#             # Send the email
#             send_mail(
#                 subject=f'New message from: {name}',
#                 message=f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}',
#                 from_email=email,
#                 recipient_list=[settings.DEFAULT_FROM_EMAIL],
#             )
#             # Redirect or render a success page
#             return redirect('contact_success')
#     else:
#         form = ContactForm()
#
#     return render(request, 'contact.html', {'form': form})

def contact(request):
    return render(request,'contact.html')

