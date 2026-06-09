# imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
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
            # Send the contact form contents as an email
            # once validation passes.
            send_mail(
                subject=form.cleaned_data["subject"],
                message=f"""
Name: {form.cleaned_data['name']}
Email: {form.cleaned_data['email']}

Message:
{form.cleaned_data['message']}
""",
                from_email=form.cleaned_data["email"],
                recipient_list=["mathew.meisinger@gmail.com"],
            )

            # Show a one-time success message after the redirect.
            messages.success(
                request,
                "Your mail has been sent! I will get back to you ASAP!"
            )
            # Redirect to avoid duplicate form submissions on page refresh.
            return redirect('home')

    # Render the homepage with either the blank form or the validated form.
    return render(request, 'main/index.html', {'form': form})
