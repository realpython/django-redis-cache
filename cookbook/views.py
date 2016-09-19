from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .services import get_recipes_without_cache as get_recipes

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def recipes_view(request):
    return render(request, 'cookbook/recipes.html', {
        'recipes': get_recipes()
    })
