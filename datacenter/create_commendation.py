from datacenter.models import Schoolkid, Subject, Teacher, Commendation


def add_commendation(text, created, schoolkid, subject, teacher):

    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid).first()
    subject = Subject.objects.filter(title=subject).first()
    teacher = Teacher.objects.filter(full_name=teacher).first()

    Commendation.objects.create(text=text, created=created, schoolkid=schoolkid, subject=subject, teacher=teacher)
