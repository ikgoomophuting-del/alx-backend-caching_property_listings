from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Retrieve all Property records, cached in Redis for 1 hour.
    """
    properties = cache.get('all_properties')

    if properties is None:
        # Cache miss → fetch from DB
        properties = list(Property.objects.all().values(
            'id', 'title', 'description', 'price', 'location', 'created_at'
        ))
        # Store in cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
        logger.info("Cache MISS: Fetched properties from DB and stored in Redis.")
    else:
        logger.info("Cache HIT: Retrieved properties from Redis.")

    return properties


def get_redis_cache_metrics():
    """
    Retrieve Redis cache performance metrics.
    Returns a dict with hits, misses, and hit ratio.
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()

    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)

    total_requests = hits + misses
    hit_ratio = (hits / total_requests) if total_requests > 0 else 0.0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 2)
    }

    logger.info(f"Redis Cache Metrics → Hits: {hits}, Misses: {misses}, Hit Ratio: {metrics['hit_ratio']}")
    return metrics
