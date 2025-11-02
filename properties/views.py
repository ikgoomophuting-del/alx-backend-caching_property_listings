from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

@cache_page(60 * 15)  # View-level cache (15 min)
def property_list(request):
    """
    Returns cached Property data from Redis (low-level caching).
    Response is also cached at view level for 15 minutes.
    """
    properties = get_all_properties()
    return JsonResponse({"data": properties})
