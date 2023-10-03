from datacenter.models import Schoolkid


def find_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено сразу несколько таких учеников')
    except Schoolkid.DoesNotExist:
        print('Ученик с таким именем не найден')
    else:
        print(schoolkid)

        return schoolkid
