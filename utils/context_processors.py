from django.contrib.auth.models import Group

def is_admin(request):
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='ADM').exists()
    else:
        is_admin = False
    return {'is_admin': is_admin}