from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Message, Article, Image, Project
from .forms import ContactForm

# Create your views here.

def index(request):
    language_preference = request.session.get('language', 'FR')
    contact_form = ContactForm()
    if language_preference == 'FR':
        return render(request, 'website/home.html', {'contact_form': contact_form})
    else:
        return render(request, 'website/home-en.html', {'contact_form': contact_form})

def contact(request):
    language_preference = request.session.get('language', 'FR')
    if language_preference == 'FR':
        return render(request, 'website/contact.html', {})
    else:
        return render(request, 'website/contact-en.html', {})

def gallery(request):
    image_list = Image.objects.all()
    page = request.GET.get('page',1)

    paginator = Paginator(image_list,4)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    if request.session.get('language', 'FR') == 'FR' :
        return render(request, 'website/gallery.html',
                  {'images': images})
    else:
        return render(request, 'website/gallery-en.html',
                  {'images': images})

def team(request):
    if request.session.get('language', 'FR') == 'FR' :
        return render(request, 'website/team.html', {})
    else:
        return render(request, 'website/team-en.html', {})


def article_list(request):
    article_list = Article.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date').reverse()
    page = request.GET.get('page',1)

    paginator = Paginator(article_list, 3)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'website/post_list.html', { 'articles': articles })

def project_list(request):
    project_list = Project.objects.filter(execution_date__lte=timezone.now()).order_by('execution_date').reverse()
    page = request.GET.get('page',1)

    paginator = Paginator(project_list, 3)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, 'website/project_list.html', { 'projects': projects })

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'website/post_detail.html', {'article': article})

def toggle_language(request):
    language_preference = request.session.get('language', 'FR')
    if language_preference == 'FR':
        request.session['language'] = 'EN'
    else:
        request.session['language'] = 'FR'
    return HttpResponseRedirect(reverse('index'))

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
            message.publication_date = timezone.now()
            message.save()

            # send_mail(subject, message, email, recipients)
            return HttpResponseRedirect(reverse('article_list'))
    else:
       return HttpResponseRedirect(reverse('article_list'))

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'website/post_detail.html',
                      {'uploaded_file_url': uploaded_file_url})

    return render(request, 'website/simple_upload.html' )

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'website/post_detail.html', {
        'form': form
    })
