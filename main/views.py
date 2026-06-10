# imports
from django.shortcuts import render


# Views for webpage
def home(request):
    """Render the main portfolio homepage."""
    return render(request, 'main/index.html')
