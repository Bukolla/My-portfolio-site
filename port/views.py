
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html', {})


def Blog(request):
    return render(request, 'blog.html', {})


def Blog2(request):
    return render(request, 'blogpage.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']

        #sendmail
        send_mail(
            message_name,  # subject
            message,      # message
            message_email,  # email to send to
            ['@gmailbukky@gmail.com', 'weareskillhub@gmail.com']
        )

        return render(request, 'base.html', {'name', message_name})
    else:
        return render(request, 'base.html', {})