from django.shortcuts import render, redirect
from .forms import bookingForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string


def bookingView(request):
    if request.method == 'POST':
        form = bookingForm(request.POST)

        if form.is_valid():

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']

            message = f"""
                Name: {firstname} {lastname}
                Email: {email}
                Contact: {contact}
                Check In: {check_in_date}
                Check Out: {check_out_date}
            """

            html = render_to_string('bookings/content.html', {
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'contact': contact,
                'check_in': check_in_date,
                'check_out': check_out_date
            })

            try:
                send_mail(firstname + " " + lastname, message, settings.EMAIL_HOST_USER,
                          ["info@boffarcabins.com"], html_message=html)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "bookings/success.html")

    else:
        form = bookingForm()

    return render(request, 'bookings/index.html', {'form': form})
