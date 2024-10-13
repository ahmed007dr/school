from .models import Settingz


def get_settings(request):
    settings_data = Settingz.objects.last()
    return{'settings_data':settings_data}