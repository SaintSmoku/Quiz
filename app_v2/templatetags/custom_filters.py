from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Custom filter to access dictionary values by key.
    """
    if dictionary and key:
        return dictionary.get(key)  # Returns the value for the key
    return None