from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import Schoolkid


def found_schoolkid(name):
    try:
        schoolkid_name = Schoolkid.objects.get(full_name__contains=name)
    except MultipleObjectsReturned:
        print('Найдено сразу несколько таких учеников')
    except ObjectDoesNotExist:
        print('Ученик с таким именем не найден')
    else:
        print(schoolkid_name)
