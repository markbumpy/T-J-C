from django.shortcuts import render, redirect
from django.views.generic import DetailView, View, ListView
from .forms import RegisterForm, ContactForm
from django.contrib import messages
from .models import *
import random
from django.core.mail import send_mail
from .models import Register, Contact


# Create your views here.

def home(request):
    items = list(Merch.objects.all())
    random.shuffle(items)
    random_products = items[:6]
    limit = items[:6]

    context = {
        'products': random_products,
        'items': limit
    }

    return render(request, 'index.html', context)



class RegisterView(View):
    def get(self, *args, **kwargs):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(self.request, 'register.html', context)
    def post(self, *args, **kwargs):
        form = RegisterForm(self.request.POST or None)
        print(self.request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            Email = form.cleaned_data.get('Email')
            phone_number = form.cleaned_data.get('phone_number')
            country = form.cleaned_data.get('country')
            register_form = Register(
                first_name=first_name,
                last_name=last_name,
                Email=Email,
                phone_number=phone_number,
                country=country,

            )
            register_form.save()
            messages.success(self.request,"your regristration was successful we'd get back to you")
            return redirect('/')
        messages.warning(self.request,"Your registration was not successful please try again")
        return redirect('register')


# class ContactView(View):
#     def get(self, *args, **kwargs):
#         form = ContactForm()
#         context = {
#             'form':form
#         }
#         return render(self.request, 'contact.html', context)
#     def post(self, *args, **kwargs):
#             form = ContactForm(self.request.POST or None)


#             if form.is_valid():
#                 name = form.cleaned_data.get('name')
#                 your_email = form.cleaned_data.get('email')
#                 message = form.cleaned_data.get('message')

#                 send_mail(
#                     name,
#                     your_email,
#                     message,
#                     ['markbumpy91@gmail.com'],
#                     fail_silently=False
#                 )
#                 message.success(self.request, "Thanks, We've received your Email, we'll respond shortly")
#                 return redirect('home')
#             messages.warning(self.request, "your registration was not successful please try again")
#             return redirect('contact')

class ContactView(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(self.request, 'contact.html', context)

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST or None)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            your_email = form.cleaned_data.get('email')
            message_body = form.cleaned_data.get('message_body')
            contact_form = Contact(
                name=name,
                your_email=your_email,
                message_body=message_body,
            )

            # Use send_mail correctly with subject, message, from_email, recipient_list
            send_mail(
                f'Contact Form Submission from {name}',
                f'Name: {name}\nEmail: {your_email}\nMessage: {message_body}',
                your_email,  # Use the sender's email address
                ['markbumpy91@gmail.com'],  # Use the recipient's email address
                fail_silently=False
            )
            contact_form.save()
            messages.success(self.request, "Thanks, We've received your Email, we'll respond shortly")
            return redirect('home')
        else:
            messages.warning(self.request, "Your message was not sent. Please check the form for errors.")
            return redirect('contact')