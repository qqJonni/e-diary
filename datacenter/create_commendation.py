from datacenter.models import Schoolkid, Subject, Teacher, Commendation


def add_commendation(text, created, schoolkid, subject, teacher):
    Commendation.objects.create(text=f'{text}', created=f'{created}', schoolkid=Schoolkid.objects.filter(full_name=f'{schoolkid}')[0], subject=Subject.objects.filter(title=f'{subject}')[0], teacher=Teacher.objects.filter(full_name=f'{teacher}')[0])


if __name__ == '__main__':
    add_commendation('Молодец!', '2018-10-02', 'Фролов Иван Григорьевич', 'Музыка', 'Селезнева Майя Макаровна')