from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache for 15 minutes (900 seconds)
def property_list(request):
    """
    Returns a JSON response of all properties.
    The response is cached in Redis for 15 minutes.
    """
    properties = Property.objects.all().values(
        'id', 'title', 'description', 'price', 'location', 'created_at'
    )
    return JsonResponse({
        "data": list(properties)
    })
