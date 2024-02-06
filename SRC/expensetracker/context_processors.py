from django.conf import settings

def get_app_wide_configs(request):
    return {
        'CURRENCY': 'USD'
    }