from django.shortcuts import render, redirect
from .forms import contactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string


def contactsView(request):
    if request.method == 'POST':
        form = contactForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            message = f"""
                Name: {firstname} {lastname}
                Email: {email}
                Query: {body}
            """

            html = render_to_string('contacts/content.html', {
                'subject': subject,
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'contact': contact,
                'subject': subject,
                'body': body,
            })

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                          ["info@boffarcabins.com"], html_message=html)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "contacts/success.html")

    else:
        form = contactForm()

    return render(request, 'contacts/index.html', {'form': form})
