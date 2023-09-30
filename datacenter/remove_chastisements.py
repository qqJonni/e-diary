from datacenter.models import Chastisement


def remove_chastisements(schoolkid):
    zam = Chastisement.objects.filter(schoolkid__full_name__contains=f'{schoolkid}')
    for z in zam:
        z.delete()
