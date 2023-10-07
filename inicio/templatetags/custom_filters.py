from django import template

register = template.Library()

@register.filter
def calculate_percentage(value, total):
    if total == 0:
        return 0.0
    return (value / total) * 100
