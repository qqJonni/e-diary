from datacenter.models import Chastisement, Schoolkid, Subject, Teacher, Commendation


def remove_chastisements(schoolkid):
    zam = Chastisement.objects.filter(schoolkid__full_name__contains=f'{schoolkid}')
    for z in zam:
        z.delete()


def add_commendation(text, created, schoolkid, subject, teacher):
    Commendation.objects.create(text=f'{text}', created=f'{created}', schoolkid=Schoolkid.objects.filter(full_name=f'{schoolkid}')[0], subject=Subject.objects.filter(title=f'{subject}')[0], teacher=Teacher.objects.filter(full_name=f'{teacher}')[0])
