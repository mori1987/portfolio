from django.shortcuts import render,redirect
from django.views import View
from . form import Contact_Form
from . models import Contact
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
import csv



class ContactView(View):
    def get(self,request):
        return render(request,'contact/contact.html')
    def post(self,request):
        return render(request,'contact/contact.html')
#

class ContactFormView(View):
    def get(self,request):
        if request.method == 'POST':
            form = Contact_Form(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                phone_number=form.cleaned_data['phone_number']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                form.save([name,phone_number, email, message])
                return redirect('contact:contact')
        else:
            form = Contact_Form()
            return render(request,'contact/contact.html',{'form':form})



        # email_subject=f'New contactform submission form{name}'
        # email_body=f'name:{name}\n phone_number:{phone_number}\n email:{email}\n message:{message}'
        # email=EmailMessage(email_subject,email_body,to=['samin198787@gmail.com'])
        # email.send()



