from datacenter.models import Chastisement


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid__full_name__contains=schoolkid).all().delete()
