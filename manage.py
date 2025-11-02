python manage.py makemigrations
python manage.py migrate
python manage.py shell


from properties.models import Property
from django.core.cache import cache

# Confirm cache is empty
print(cache.get('all_properties'))

# Generate and store the cache
list(Property.objects.all().values())
cache.set('all_properties', "test_data", 3600)
print(cache.get('all_properties'))  # Should show 'test_data'

# Create a Property to trigger post_save
Property.objects.create(title="Test", description="Signal test", price=1000, location="Cape Town")

# Check cache again
print(cache.get('all_properties'))  # Should now be None (invalidated)
