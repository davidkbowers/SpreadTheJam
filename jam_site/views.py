import secrets
import string
from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .forms import ContactForm, NewsletterForm
from .models import Article, Band, Show, Contact, Newsletter


@receiver(user_signed_up)
def send_subscribe_email(**kwargs):
    user = kwargs['user']
    #instance = User.objects.get_by_natural_key(kwargs['user'])
    text_content = 'Thank you for signing up for the Spread The Jam newsletter. We will keep you informed about the bands you love and their upcoming shows.'
    html_content = render_to_string('subscribe_email.html', {'name': user.username})
    #send_email(user.email, text_content, html_content)


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            c = Contact()
            c.name = name
            c.email = email
            c.message = message
            c.send_copy = copy
            c.answered = False
            c.reference = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(15))
            if request.user.is_authenticated:
                c.user_id = request.user.id
            c.save()

            #text_content = 'Thank you for sending us a message. We will get back to you as soon as possible.'
            #html_content = render_to_string('contact_email.html', {'name': name})
            #send_email(email, text_content, html_content)

            messages.success(request, 'Contact request submitted successfully.')
            form1 = ContactForm()
            return render(request, 'contact.html', {'form': form1})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')


class BandsListView(ListView):
    model = Band
    context_object_name = 'bands'
    template_name = 'bands.html'


class ArticlesListView(ListView):
    context_object_name = 'articles'
    paginate_by = 12
    template_name = 'news.html'

    def get_queryset(self):
        today = date.today()
        back_year = today - relativedelta(years=5)
        return Article.objects.filter(date_published__gte=back_year, date_published__lte=today).order_by('-date_published')

class ShowsListView(ListView):
    #model = Show
    context_object_name = 'shows'
    paginate_by = 12
    template_name = 'shows.html'

    def get_queryset(self):
        today = date.today()
        next_year = today + relativedelta(years=1)
        return Show.objects.filter(event_date__gte=today, event_date__lte=next_year).order_by('event_date')


class SearchListView(ListView):
    #model = Show
    context_object_name = 'search'
    paginate_by = 12
    template_name = 'search.html'

    def get_queryset(self):
        today = date.today()
        next_year = today + relativedelta(years=1)
        return Show.objects.filter(event_date__gte=today, event_date__lte=next_year).order_by('event_date')

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            newsletter = Newsletter()
            newsletter.name = name
            newsletter.email = email
            if request.user.is_authenticated:
                newsletter.user_id = request.user.id
            newsletter.save()

            text_content = """Thank you for signing up for the spreadthejam.band newsletter. Each issue gives you the latest news about the bands you love and their upcoming shows.
            
            If you sign up you can pick the bands you are interested in and your news and shows will only be fore those bands.
            
            Thank you for your interest in Spread The Jam."""

            #html_content = render_to_string('newsletter.html', {'name': name})
            #send_email(email, text_content, html_content)



            messages.success(request, 'Newsletter signup submitted successfully.')
            form1 = NewsletterForm()
            return render(request, 'newsletter_success.html', {'form': form1})
    else:
        form = NewsletterForm()
        return render(request, 'newsletter.html', {'form': form})


def send_email(email, text_mail, html_mail):
    smtp_server = "smtp.fastmail.com"
    port = 465  # For SSL
    sender_email = "team@spreadthejam.band"
    password = 'fktsnyh33h453zvk'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Spread The Jam Contact request received"
    message["From"] = sender_email
    message["To"] = email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text_mail, "plain")
    part2 = MIMEText(html_mail, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, email, message.as_string()
        )