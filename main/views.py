# imports
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

from .forms import ContactForm


# Views for webpage
def home(request):
    '''
    This view will render the main page for the portfolio.
    Will return using the imported render method from Django
    and will call the main homepage.
    This View will also allow the user to send an email to me.
    '''
    # Start with an empty contact form for the initial page load.
    form = ContactForm()

    if request.method == "POST":
        # Rebuild the form with submitted data so Django can validate it.
        form = ContactForm(request.POST)

        if form.is_valid():
            # Send the contact form contents as an email once validation passes.
            try:
                email_body = """
Name: {name}
Email: {email}

Message:
{message}
""".strip().format(
                    name=form.cleaned_data["name"],
                    email=form.cleaned_data["email"],
                    message=form.cleaned_data["message"],
                )

                email = EmailMessage(
                    subject=form.cleaned_data["subject"],
                    body=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_RECIPIENT_EMAIL],
                    reply_to=[form.cleaned_data["email"]],
                )
                email.send(fail_silently=False)

                # Show a one-time success message after the redirect.
                messages.success(
                    request,
                    "Your mail has been sent! I will get back to you ASAP!"
                )
                # Redirect to avoid duplicate form submissions on page refresh.
                return redirect('home')
            except Exception:
                messages.error(
                    request,
                    "Sorry, your message could not be sent right now. "
                    "Please try again later."
                )

    # Render the homepage with either the blank form or the validated form.
    return render(request, 'main/index.html', {'form': form})
