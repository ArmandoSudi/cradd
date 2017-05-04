from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Message
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'website/index.html', {})

def hello(request):
    return render(request, 'website/base.html', {})

def home(request):
    contact_form = ContactForm()
    return render(request, 'website/home.html', {'contact_form': contact_form})

def contact(request):
    return render(request, 'website/contact.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request , 'website/post_list.html', {'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'website/post_detail.html', {'post':post})

def get_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipients = ['armando.sudi@gmail.com']

            message = Message(name=name, email=email, subject=subject, message=message)
            message.save()

            # send_mail(subject, message, email, recipients)
            return HttpResponseRedirect(reverse('post_list'))
    else:
       return HttpResponseRedirect(reverse('post_list'))

def test(request):
    return HttpResponseRedirect(reverse('post_list'))
