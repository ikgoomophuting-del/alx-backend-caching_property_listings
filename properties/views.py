from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache this view for 15 minutes
def property_list(request):
    """
    View to display all properties.
    Cached for 15 minutes using Redis as the backend.
    """
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})
  
