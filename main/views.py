# imports
from django.shortcuts import render


# Views for webpage
def home(request):
    '''
    This view will render the main page for the portfolio.
    Will return using the imported render method from Django
    and will call the main homepage.
    This View will also allow the user to send an email to me.
    '''
    return render(request, 'main/index.html')
